from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date+"/")

soup = BeautifulSoup(response.text, 'html.parser')
chart = soup.find("div", class_="lxml")

song_names_initial = [x.getText() for x in soup.select("div.chart-results-list > div.o-chart-results-list-row-container"
                                                       " > ul.o-chart-results-list-row > li:nth-child(4) > ul > "
                                                       "li:nth-child(1) h3")]
author_names_initial = [x.getText() for x in soup.select("div.chart-results-list > div.o-chart-results-list-"
                                                         "row-container > ul.o-chart-results-list-row > li:"
                                                         "nth-child(4) > ul > li:nth-child(1) span")]
song_names = []
author_names = []
[song_names.append(song.strip((' \n\t'))) for song in song_names_initial]
[author_names.append(author.strip(' \n\t')) for author in author_names_initial]
# [print(song) for song in song_names]
with open("songs.txt", "w", encoding="utf-8") as file:
    file.truncate(0) # clear file before to write in it
    for item in song_names:
        file.write(item + "\n")

# print(len(author_names))

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="ea29c53300254020a0baf8fb46c0f930",
        client_secret="fa1ff2849ae140cc942c3b8b262c69c6",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0] # take year from user input date
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f" Skipped. {song} doesn't exist in Spotify.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


