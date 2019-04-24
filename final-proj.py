# Enter your twitter info here

import requests
import json

def artistsearch(artist):
    r = requests.get('http://itunes.apple.com/search', params= {
        'term': artist,
        'entity': 'song',
        'limit':20 #need to limit what's added to database
    })

    result = json.loads(r.text)
    data = result['results']

    songTime_list = []

    for item in data:
        timeMS = item['trackTimeMillis']
        time = int(timeMS) / 60000
        songTime_list.append(time)
 
    totaltime = 0 
    for time in songTime_list:
        totaltime += time
        songs = len(songTime_list)
        avg = totaltime/songs
    
    return avg
   
avgsong_John = artistsearch('John Mayer')
avgsong_Frank = artistsearch('Frank Ocean')
avgsong_Bob = artistsearch('Bob Marley')

print(avgsong_Bob)
print(avgsong_Frank)
print(avgsong_John)

    