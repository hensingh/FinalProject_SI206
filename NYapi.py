import requests
import json
import sqlite3
import os

#source_dir = os.path.dirname
#full_path = os.path.join(source_dir, )
#file = open(full_path, 'r')

#key = 'YG8Tktps3JKniMJohga7kO5f5WecrgW6'
#conn = sqlite3.connect('/Users/andrewkaiser/Documents.sqlite')


conn = sqlite3.connect('/Users/andrewkaiser/Documents/finalproject.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS nytimes')
cur.execute('CREATE TABLE nytimes (section TEXT, length INTEGER)')
#conn.close()

def nyUS():
    #mostviewed = requests.get('https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?limit=2&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/U.S./168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    nyUS_list = []
    for item in ny_obj['results']:
        nyUS_list.append(len(item['title']))
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))
        #conn.commit()
        #print(len(item['title']))
    #conn.commit()

    #total = 0
    #for x in nyUS_list:
        #total += x
    #avg_len = total/len(nyUS_list)

    #print(avg_len)
    #return avg_len

def nyWORLD():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/World/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    nyWORLD_list = []
    for item in ny_obj['results']:
        nyWORLD_list.append(len(item['title']))
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))
        #conn.commit()
        #print(len(item['title']))

   #total = 0
    #for x in nyWORLD_list:
        #total += x
    #avg_len = total/len(nyWORLD_list)

    #print(avg_len)
    #return avg_len

def nySPORTS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/Sports/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    nySPORTS_list = []
    for item in ny_obj['results']:
        nySPORTS_list.append(len(item['title']))
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))
        #conn.commit()

def nyBUSINESS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/Business/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    nyBUSINESS_list = []
    for item in ny_obj['results']:
        nyBUSINESS_list.append(len(item['title']))
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))
        #conn.commit()

def nyBOOKS():
    ny = requests.get('https://api.nytimes.com/svc/news/v3/content/nyt/Books/168.json?limit=20&api-key=YG8Tktps3JKniMJohga7kO5f5WecrgW6')
    ny_obj = json.loads(ny.text)

    nyNY_list = []
    for item in ny_obj['results']:
        nyNY_list.append(len(item['title']))
        cur.execute('INSERT INTO nytimes (section, length) VALUES(?,?)', (item['section'], len(item['title'])))
        #conn.commit()





    
    
#cur.close()


    #print(json.dumps(ny_obj, indent = 2))

nyUS()
nyWORLD()
nySPORTS()
nyBOOKS()
nyBUSINESS()


conn.commit()






