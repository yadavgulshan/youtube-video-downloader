import json
from youtubesearchpython import SearchVideos
import os
from bs4 import BeautifulSoup as bs4
import requests
headers = {
    'User-Agent': 'Mozilla/5.0'
}

name = "bewafa tera maasom chehra"
search_link = f"https://www.music.youtube.com/search?q={name.replace(' ','+')}"
# working with bs4 !
page = requests.get(search_link, headers=headers)
soup = bs4(page.text, 'html.parser')
print(soup.prettify())
search_part = soup.findAll(
    'a', class_="yt-simple-endpoint style-scope yt-formatted-string")
# for ytmusic in search_part:
#     yt = ytmusic.find('href')
#     print(yt)
print(search_part)

# 3
# download part
# search = SearchVideos(name, offset=1,
#                       mode="json", max_results=1)

# result = search.result()
# result = json.loads(result)
# print(result["search_result"][0]["link"])
# # link = result["search_result"][0]["link"]
# os.system(f'youtube-dl -x --playlist-end 1 --audio-format flac {link}')
# 3

# print(something['search_result'])
# print(repr(result)[:100])
# print(json.loads(result["link"]))
# print(type(result))


# YTMusic.setup(filepath='headers_auth.json', headers_raw="headers_auth.json")
# ytmusic = YTMusic('headers_auth.json')
# playlistId = ytmusic.create_playlist("test", "test description")
# search_results = ytmusic.search(name)
# ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
# print(search_results)
