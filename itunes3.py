import requests
import json
import sqlite3
import os

conn = sqlite3.connect('/Users/hennasingh/Desktop/itunes4.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Itunes')
cur.execute('CREATE TABLE Itunes(Artist TEXT, Length INTEGER)')

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
        cur.execute('INSERT INTO Itunes (Artist, Length) VALUES(?,?)', (item['artistName'], time))

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
        cur.execute('INSERT INTO Itunes (Artist, Length) VALUES(?,?)', (item['artistName'], time))     

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
        cur.execute('INSERT INTO Itunes (Artist, Length) VALUES(?,?)', (item['artistName'], time)) 

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
        cur.execute('INSERT INTO Itunes (Artist, Length) VALUES(?,?)', (item['artistName'], time))

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
        cur.execute('INSERT INTO Itunes (Artist, Length) VALUES(?,?)', (item['artistName'], time)) 
 
    #totaltime = 0 
    #for time in songTime_list:
        #totaltime += time
        #songs = len(songTime_list)
        #avg = totaltime/songs
    
    #return avg
   
John()
Frank()
Kanye()
Billie()
Justin()



conn.commit()