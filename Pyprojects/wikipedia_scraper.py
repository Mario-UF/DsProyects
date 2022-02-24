import requests
from bs4 import BeautifulSoup
import webbrowser

source = requests.get('https://es.wikipedia.org/wiki/Wikipedia:Portada').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

panel = soup.find('div', id='mw-panel')
link = panel.find('li', id='n-randompage').a['href']
randomart = f'https://es.wikipedia.org/{link}'

url_history = []
history_pos = 0

class Article:
    def __init__ (self, article_url):
        self.url = requests.get(article_url).url
        source = requests.get(self.url).text
        soup = BeautifulSoup(source,'lxml')
        self.art_title = soup.find('h1').text
        self.art_frst_ph = soup.find('div', id='mw-content-text').p.text

    def label_update(self):
        titlelab.config(text=self.art_title)
        previewlab.config(text=self.art_frst_ph.rstrip(), relief=tk.SUNKEN, bg='white')

def random_art(page):
    global history_pos
    article_shw = Article(page)
    article_shw.label_update()
    url_history.append(article_shw)
    history_pos += 1
    Gobutton.config(state='normal')

    if history_pos > 1:
        Pbutton.config(state='normal')

def art_open():
    webbrowser.open(url_history[history_pos-1].url)

def preview():
    global history_pos
    if history_pos > 2:
        history_pos -= 1
    else:
        history_pos -= 1
        Pbutton.config(state='disabled')

    show_button.config(state='disabled')
    Nbutton.config(state='normal')
    url_history[history_pos-1].label_update()

def nextt():
    global history_pos
    if history_pos < len(url_history)-1:
        history_pos += 1
    else:
        history_pos += 1
        Nbutton.config(state='disabled')
        show_button.config(state='normal')
    Pbutton.config(state='normal')

    url_history[history_pos-1].label_update()


import tkinter as tk

root = tk.Tk()
root.title('Random wikipedia article')
root.geometry('600x200')

frame = tk.Frame(root)
frame.pack(anchor='center')

show_button = tk.Button(frame,text='Show me a new random article', command=lambda : random_art(randomart))
Gobutton = tk.Button(frame,text='Let\'s go to the article', command=art_open, state='disabled',bg='blue',fg='white', font=("Helvetica", 10))
Nbutton = tk.Button(frame, text='>>',bg='red', state='disabled', command=nextt)
Pbutton = tk.Button(frame, text='<<',bg='red', state='disabled', command=preview)
titlelab = tk.Label(frame, wraplengt=400, height=2, font=('arial bold',12))
previewlab = tk.Label(frame, wraplengt=500)  # wraplengt defines a new line after certain length

show_button.pack(side='top',pady=10)
Nbutton.pack(side='right')
Pbutton.pack(side='left')
Gobutton.pack(side='bottom',pady=10)
previewlab.pack(side='bottom')
titlelab.pack(side='bottom')

tk.mainloop()

# Future improvement:
    # show me a photo
    # making my own random navigation algorithm in wikipedia
    # adding a topic subgroup