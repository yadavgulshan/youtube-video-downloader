import json
from youtubesearchpython import SearchVideos
import os
name = "bewafa tera maasom chehra"
search_link = f"https://www.youtube.com/search?q={name.replace(' ','%20')}"


# download part
search = SearchVideos(name, offset=1,
                      mode="json", max_results=1)

result = search.result()
result = json.loads(result)
link = result["search_result"][0]["link"]
os.system(f'youtube-dl -x --playlist-end 1 --audio-format flac {link}')
