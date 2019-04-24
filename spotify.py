import spotipy
import os
import sys
import sqlite3
import spotify_info
import json
from json.decoder import JSONDecodeError
import plotly
import plotly.plotly as py
import spotipy.util as util
import plotly.graph_objs as go
from plotly.graph_objs import *


username = spotify_info.username
scope = 'user-top-read'
client_id = spotify_info.client_id
client_secret = spotify_info.client_secret
redirect_uri = spotify_info.redirect_uri
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

spotify_object = spotipy.Spotify(auth=token)


conn = sqlite3.connect('spotify.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Spotify_Top_Songs (id INTEGER PRIMARY KEY, 'Song' TEXT UNIQUE, 'artist' TEXT, 'Album' TEXT, 'Popularity' INTERGER)''')
print('Connecting to Spotify API and Creating Database')



# spotify = spotipy.Spotify(auth = token)s
'''for count in range(0,100,10):
	name = 'Anderson .Paak'
	results = spotify_object.search(q='artist:' + name, offset='{}'.format(count),type='track', market='US')
	for item in results['tracks']['items']:
		name = item['name']
		try:
			album = item['album']['name']
		except:
			album = None
		try:
			popularity = item['popularity']
		except:
			popularity = None
		print(name, album, popularity)'''

def insert_data():
	user_top_tracks = spotify_object.current_user_top_tracks(limit=100,offset=0,time_range='long_term')
	for x in user_top_tracks['items']:
		name = x['name']
		artist = x['artists'][0]['name']
		album = x['album']['name']
		popularity = x['popularity']
		cur.execute('INSERT OR IGNORE INTO Spotify_Top_Songs (Song, artist, Album, Popularity) VALUES (?, ?, ?, ?)', (name, artist, album, popularity))
	conn.commit()
if __name__ == "__main__":
    insert_data()
