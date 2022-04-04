import json
import os

# spotipy documentation: https://github.com/plamere/spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Personal Spotify Credentials - https://developer.spotify.com/dashboard/login
client_id = '****'
client_secret = '****'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_id = 'spotify:user:spotifycharts:playlist:4vKSQjBWzGfVy10Sx41EMf'  # my personal list URI
load_batch = 100  # number of tracks to parse for each loop

# EXTRACT JSON
offset = 0  # start from the first row
list_songs = []
while True:
    
    my_playlist = sp.playlist_items(playlist_id,
                                    offset=offset, 
                                    limit=load_batch,
                                    additional_types=['track'])

    if len(my_playlist['items']) == 0:
        break
    
    #print(json.dumps(list_songs, indent=5))  #check json as string

    list_songs += my_playlist['items']

    offset += len(my_playlist['items'])
    print(offset, "/", my_playlist['total'])

with open('spotify.json', 'w') as f:
        json.dump(list_songs, f, indent=4)