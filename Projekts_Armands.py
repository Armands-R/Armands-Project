import json
import sys
import sqlite3
import requests

global dati
                                                                                                                                                                                                                    # from bs4 import BeautifulSoup
connection = sqlite3.connect("main.db")

# https://www.stands4.com/services/v2/lyrics.php?uid=12502&tokenid=xhIwZZuaJqWznHSV&term=forever%20young&artist=Alphaville&format=json


word = input("Ievadi vienu vārdu angliski: ")
headers = {'User-Agent': 'Mozilla/5.0'}
dati = requests.get(f"https://www.stands4.com/services/v2/lyrics.php?uid=12502&tokenid=xhIwZZuaJqWznHSV&term={word}&format=json", headers=headers).json()
# print(f"https://www.stands4.com/services/v2/lyrics.php?uid=12502&tokenid=xhIwZZuaJqWznHSV&term={word}&format=json")
# print(dati)
                                                                                                                                                                                                                # zupa = BeautifulSoup(dati.content, "html.parser")
                                                                                                                                                                                                                # rez = str(zupa.find("div", {"class":"json-scrolling-panel"}))
                                                                                                                                                                                                                # print(rez)
# a

# with open('lyrics.json', 'r') as f:
#     data = json.load(f)
# print(data)

                 

# for artist in data.keys():                                       
#     print(artist)




# def count_artists(dati):
#     with open(dati, 'r') as f:
#         data = json.load(f)
#         artists = [entry['artist'] for entry in data['result']]
#         artist_count = len(artists)
#         return artist_count


# count = count_artists(dati)
# print("Count of 'artist' key:", count)




def count_artists(dati):
    kopa = set()
    sk = 0
    for el in dati['result']:
        # print(el['artist'])
        kopa.add(el['artist'])
    # artists = [entry['artist'] for entry in data['result']]
    # artist_count = len(artists)
    # print(dati['result'])
    print(kopa)
    return len(kopa)


count = count_artists(dati)
print("Count of 'artist' key:", count)







# def count_selected_keys(json_data, selected_keys):
#     counts = {key: 0 for key in selected_keys}

#     for item in json_data:
#         for key in selected_keys:
#             if key in item:
#                 counts[key] += 1

#     return counts

# json_data = dati.json()

# selected_keys = ['artist']

# key_counts = count_selected_keys(json_data, selected_keys)
# # key_counts = json_data['result'].count()

# for key, count in key_counts.items():
#     print(f"{key}: {count}")



















































# klienta2_id = "EIpcEal2Kdlck9COc_CzfCzalsdu_xzwxqmSTvKQy6AuJTVdyXwB5zBBKxPo3pBH"
# klienta2_secret = "B2AkQktsf5qq0rP4WMwLX7xcN8kbMql4pq35i9se7zGDPG-zU_AEpfM1tBwq9rNsQ3v4xHIPgeuCV2XskeA-sQ"
# access_token = "BIH3Ig-66qBCiX8qFFIrm81B7A1p5aKOPydarK_0YNRZO25kauVOZAWpTYRhKCop"


# artist= input("Ieraksti izpildītāju: ")
# song = input("Ieraksti dziesmas nosaukumu: ")


# Authorozation = access_token
# GET /some-endpoint HTTP/1.1
# User-Agent: CompuServe Classic/1.22
# Accept: application/json
# Host: api.genius.com
# Authorization: Bearer ACCESS_TOKEN


# https://docs.genius.com/#/getting-started-h1

# def get_song_lyrics(artist_name, song_title, access_token):
#     base_url = "https://api.genius.com"
#     search_url = base_url + "/search"
#     headers = {"Authorization": "Bearer " + access_token}
#     params = {"q": song_title + " " + artist_name}
#     print(search_url)

#     response = requests.get(search_url, params=params, headers=headers)
#     data = response.json()
#     print(json.dumps(data["response"]))
#     hits = data["response"]["hits"]
    
#     if hits:
#         # pienemot ka pirma dziesma kas uzradas ir ista
#         song_path = hits[0]["result"]["api_path"]
#         song_url = base_url + song_path
#         response = requests.get(song_url, headers=headers)
        
        
#         # izvelk dziesmu vardus
#         song_lyrics = response.json()["response"]["hits"]["song"]["lyrics"]
#         return song_lyrics
#     else:
#         return "Song not found."


# access_token = "BIH3Ig-66qBCiX8qFFIrm81B7A1p5aKOPydarK_0YNRZO25kauVOZAWpTYRhKCop"
# artist_name = artist
# song_title = song

# lyrics = get_song_lyrics(artist_name, song_title, access_token)
# print("Lyrics for '{}' by {}:".format(song_title, artist_name))
# print(lyrics)