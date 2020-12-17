import json
from youtubesearchpython import SearchVideos
import os
YesorNo = input("Do you have a link or you want me to search ?\n1. Yes I have a link\n2. No, I want to search the name and want to download the first video in query\n:")
if (YesorNo == 1):
    link = input("Please input your link: ")
else:
    name = input("Name of video to download: ")
    search_link = f"https://www.youtube.com/search?q={name.replace(' ','%20')}"
    search = SearchVideos(name, offset=1,
                          mode="json", max_results=1)
    result = search.result()
    result = json.loads(result)
    link = result["search_result"][0]["link"]

os.system(f'youtube-dl -f best {link}')
print("Video link: ", link)
