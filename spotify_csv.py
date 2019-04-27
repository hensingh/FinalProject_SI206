import os
import sys
import json
from json.decoder import JSONDecodeError
import sqlite3
import csv

def spotify_csv():
    print("Beginning process")
    conn = sqlite3.connect('spotify.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT album, AVG(Popularity) FROM Spotify_Top_Songs GROUP BY album ORDER BY album")

    album_name = {}
    data = []
    for row in cur:
        try:
            data.append(row)
        except:
            print('encoding error')
    
    for tup in data:
        album = tup [0]
        popularity = tup[1]
        if album not in album_name.keys():
            album_name[album] = [popularity]
        else:
            album_name[album].append(popularity)
    
    for item in album_name.items():
        average = sum(item[1])/len(item[1])
        album_name[item[0]] = int(average)

    
    sorted_list_1 = sorted(album_name.items(), key=lambda x: x[0])
    with open('spotify__albums.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(sorted_list_1)
    csvFile.close()  
    print("Process ended")
    print("")
    print("Creating Spotify Album Data.")



if __name__ == "__main__":
    spotify_csv()
