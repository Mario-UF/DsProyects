import json
import pandas as pd
import numpy as np

# spotipy documentation: https://github.com/plamere/spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Personal Spotify Credentials - https://developer.spotify.com/dashboard/login - It is needed to create an aplication in spotify dev page.
client_id = '*****'
client_secret = '******'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_id = 'spotify:user:spotifycharts:playlist:4vKSQjBWzGfVy10Sx41EMf'  # my personal list URI
load_batch = 100  # number of tracks to parse for each loop

# EXTRACT EVERY TRACK IN THE LIST:
offset = 0  # start from the first row
songs_list = []
while True:
    my_playlist = sp.playlist_items(playlist_id,
                                    offset=offset, 
                                    limit=load_batch,
                                    additional_types=['track'])

    if len(my_playlist['items']) == 0:
        break

    songs_list += my_playlist['items']

    offset += len(my_playlist['items'])
    print(offset, "/", my_playlist['total'])

track_names_and_first_artist = []   # there can be more than one artist in the song, for simplicity we choose only the first one.
for i in songs_list:
    track_names_and_first_artist.append([i['track']['name'], i['track']['artists'][0]['name']])
    # other future interesting attributes: ['popularity'], ['album'], ['album']['release_date'] (this is the way we can extract the song release date)


# EXTRACT AUDIO FEATURES FOR EVERY TRACK IN THE LIST: 
track_ids = []
for i in songs_list:
    track_ids.append(i['track']['id'])

songs_features_obj = []
track_idx=0
while track_idx < len(songs_list):
    songs_features_obj += sp.audio_features(tracks=track_ids[track_idx:track_idx+100]) # max 100 ids per loop (documentation)
    track_idx += 100

songs_features = []
for f in songs_features_obj:
    songs_features.append([f['danceability'],f['energy'],f['loudness'],f['key'],f['mode'],f['speechiness']
                        ,f['acousticness'],f['instrumentalness'],f['liveness'],f['valence'],f['tempo']
                        ,f['duration_ms'],f['time_signature'],f['uri']])


df_song = pd.DataFrame(track_names_and_first_artist,columns=['name','artist'])
df_feat = pd.DataFrame(songs_features, columns=['danceability','energy','loudness','key','mode','speechiness'
                        ,'acousticness','instrumentalness','liveness','valence','tempo'
                        ,'duration_ms','time_signature','uri'])

df = pd.concat((df_song,df_feat), axis=1)

df.to_csv('myspotifylist.csv')