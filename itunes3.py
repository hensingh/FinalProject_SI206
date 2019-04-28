import requests
import json
import sqlite3
import os
import plotly
import plotly_info

import plotly.graph_objs as go
import plotly.plotly as py
from plotly.graph_objs import *

plotly.tools.set_credentials_file(username='hensingh', api_key="kzdkwuy8LmYE0Njvb0OD")
conn = sqlite3.connect('/Users/hennasingh/Desktop/itunes5.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Itunes')
cur.execute('CREATE TABLE Itunes(Length INTEGER, Artist TEXT)')
def test():
    pass
def John():
    r = requests.get('http://itunes.apple.com/search', params= {
        'term': 'John Mayer',
        'entity': 'song',
        'limit':20 #need to limit what's added to database
    })

    result = json.loads(r.text)
    data = result['results']

    for item in data:
        timeMS = item['trackTimeMillis']
        time = int(timeMS) / 60000
        cur.execute('INSERT INTO Itunes (Length, Artist) VALUES(?,?)', (time, item['artistName']))

def Frank():
    r = requests.get('http://itunes.apple.com/search', params= {
        'term': 'Frank Ocean',
        'entity': 'song',
        'limit':20 #need to limit what's added to database
    })

    result = json.loads(r.text)
    data = result['results']

    for item in data:
        timeMS = item['trackTimeMillis']
        time = int(timeMS) / 60000
        cur.execute('INSERT INTO Itunes (Length, Artist) VALUES(?,?)', (time, item['artistName'])) 

def Kanye():
    r = requests.get('http://itunes.apple.com/search', params= {
        'term': 'Kanye West',
        'entity': 'song',
        'limit':20 #need to limit what's added to database
    })

    result = json.loads(r.text)
    data = result['results']

    for item in data:
        timeMS = item['trackTimeMillis']
        time = int(timeMS) / 60000
        cur.execute('INSERT INTO Itunes (Length, Artist) VALUES(?,?)', (time, item['artistName']))

def Billie():
    r = requests.get('http://itunes.apple.com/search', params= {
        'term': 'Billie Eilish',
        'entity': 'song',
        'limit':20 #need to limit what's added to database
    })

    result = json.loads(r.text)
    data = result['results']

    for item in data:
        timeMS = item['trackTimeMillis']
        time = int(timeMS) / 60000
        cur.execute('INSERT INTO Itunes (Length, Artist) VALUES(?,?)', (time, item['artistName']))

def Justin():
    r = requests.get('http://itunes.apple.com/search', params= {
        'term': 'Justin Bieber',
        'entity': 'song',
        'limit':20 #need to limit what's added to database
    })

    result = json.loads(r.text)
    data = result['results']

    for item in data:
        timeMS = item['trackTimeMillis']
        time = int(timeMS) / 60000
        cur.execute('INSERT INTO Itunes (Length, Artist) VALUES(?,?)', (time, item['artistName']))
 


John()
Frank()
Kanye()
Billie()
Justin()


conn.commit()

cur.execute('SELECT * FROM Itunes')
artistsonglength = []
for row in cur: 
    artistsonglength.append(row)

johnL = []
frankL = []
kanyeL = []
billieL = []
justinL = []
for tup in artistsonglength:
    time = tup[0]
    artist = tup[1]
    if 'John Mayer' in artist:
        johnL.append(time)
    if 'Frank Ocean' in artist:
        frankL.append(time)
    if 'Kanye West' in artist:
        kanyeL.append(time)
    if 'Billie Eilish' in artist:
        billieL.append(time)
    if 'Justin Bieber' in artist:
        justinL.append(time)

outfile = open('itunesapi.csv', 'w')

johnsum = 0
for num in johnL:
    johnsum += num
    johnavg = round(johnsum / len(johnL),2)
outfile.write(('John, {}'.format(johnavg))+'\n')


franksum = 0
for num in frankL:
    franksum += num
    frankavg = round(franksum / len(frankL),2)
outfile.write(('Frank, {}'.format(frankavg))+'\n')

kanyesum = 0
for num in kanyeL:
    kanyesum += num
    kanyeavg = round(kanyesum / len(kanyeL),2)
outfile.write(('Kanye, {}'.format(kanyeavg))+'\n')

billiesum = 0
for num in billieL:
    billiesum += num
    billieavg = round(billiesum / len(billieL),2)
outfile.write(('Billie, {}'.format(billieavg))+'\n')

justinsum = 0
for num in justinL:
    justinsum += num
    justinavg = round(justinsum / len(justinL),2)
outfile.write(('Justin, {}'.format(justinavg))+'\n')

outfile.close()
conn.commit()


def viz():
    artists = []
    songavg = []
    file = open('itunesapi.csv','r')
    x= (file.readlines())
    
    for item in x:
        cells = item.split(',')
        artists.append(cells[0])
        songavg.append(cells[1].strip('\n'))
    print(songavg)

    data = [go.Bar(x=artists, y=songavg)]
    
    layout = go.Layout(
        title = 'Artists Average Song Length',
        yaxis=dict(title="Avg Song Length", range=[0,5])
        
    )


    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename="Artists Average Song Length")

    
    
    
    
    
        
    
viz()


cur.close()