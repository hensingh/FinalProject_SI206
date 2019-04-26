import sqlite3

import plotly
import plotly.graph_objs as go
import plotly.plotly as py
import spotipy
import spotipy.util as util
from plotly.graph_objs import *

import spotify_info

username = spotify_info.username
scope = 'user-top-read'
client_id = spotify_info.client_id
client_secret = spotify_info.client_secret
redirect_uri = spotify_info.redirect_uri
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

spotify_object = spotipy.Spotify(auth=token)


conn = sqlite3.connect("spotify.sqlite")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Spotify_Top_Songs (id INTEGER PRIMARY KEY, 'Song' TEXT UNIQUE, 'artist' TEXT, 'Album' TEXT, 'Popularity' INTERGER)''')
print('Connecting to Spotify API and Creating Database')


def insert_data(artist_name):

	for count in range(0,100,10):
		results = spotify_object.search(q='artist:' + artist_name,limit=10, offset=count,type='track', market='US')
		for item in results['tracks']['items']:
			name = item['name']
			artist = item["artists"][0]["name"]
			try:
				album = item['album']['name']
			except:
				album = None
			try:
				popularity = float(item['popularity'])
			except:
				popularity = None
			cur.execute(
	                "INSERT OR IGNORE INTO Spotify_Top_Songs (Song, artist, Album, Popularity) VALUES (?, ?, ?, ?)",
	                (name, artist, album, popularity),
	            )
			conn.commit()


def viz():
    cur = conn.cursor()
    cur.execute(
        "SELECT album, AVG(Popularity) FROM Spotify_Top_Songs GROUP BY album ORDER BY album"
    )
    album = []
    popularity = []
    for row in cur:
        album.append(row[0])
        popularity.append(float(row[1]))

    data = [go.Bar(x=album, y=popularity)]
    layout = go.Layout(
        title="Albums and Their Average Popularity",
        yaxis=dict(title="Popularity")
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename="Artists and Their Average Popularity")


if __name__ == "__main__":
    artist = input('Enter Artist: ')
    insert_data(artist)
    viz()
    conn.close()
