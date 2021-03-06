import requests
import json
import sqlite3
import os
import plotly
import plotlyinfo

import plotly.graph_objs as go
import plotly.plotly as py
from plotly.graph_objs import *


plotly.tools.set_credentials_file(username='arkaiser', api_key='FPD9QHLidggsZLawfmQh')


conn = sqlite3.connect('spotify.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS nytimes (section TEXT, length INTEGER)')
#conn.close()

def nyUS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/U.S./168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    for item in ny_obj['results']:
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))

def nyWORLD():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/World/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    for item in ny_obj['results']:
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))

def nySPORTS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/Sports/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    for item in ny_obj['results']:
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))

def nyBUSINESS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/Business/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    for item in ny_obj['results']:
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))

def nyBOOKS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/Books/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    for item in ny_obj['results']:
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))
     
#cur.close()


nyUS()
nyWORLD()
nySPORTS()
nyBOOKS()
nyBUSINESS()

conn.commit()


def viz():
    cur.execute('SELECT section, AVG(length) FROM nytimes GROUP BY section ORDER BY section')
    outfile = open('nyapi.txt', 'w')
    section = []
    avglength = []
    for x in cur:
        section.append(x[0])
        avglength.append(x[1])
    outfile.write(str(section) + str(avglength))
    outfile.close()
    conn.commit()
   
    dt = [go.Bar(x=section, y=avglength, marker = dict(color='rgb(45,20,75)'))]
    lo = go.Layout(title='NY Times Sections and Their Average Title Lengths', yaxis=dict(title='Average Title Length'))

    fig = go.Figure(data=dt, layout=lo)
    py.plot(fig, filename = 'NYTIMES')




viz()