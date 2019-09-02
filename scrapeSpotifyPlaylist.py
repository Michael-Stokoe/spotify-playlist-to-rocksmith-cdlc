from selenium import webdriver
webdriver.ChromeOptions.binary_location = ur"C:\\Program Files (x86)\\Google\\Chrome Beta\\Application\\chrome.exe"


def get_songs_from_spotify(spotify_playlist_url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get(spotify_playlist_url)

    song_list = driver.find_element_by_css_selector('ol.tracklist')

    artist_elements = song_list.find_elements_by_css_selector('a.tracklist-row__artist-name-link')
    title_elements = song_list.find_elements_by_css_selector('div.tracklist-name')

    artists = []
    titles = []

    for element in artist_elements:
        artists.append(element.text)
        
    for element in title_elements:
        titles.append(element.text)
        
    if len(artists) != len(titles):
        print("Weird thing happened. Aritsts and song-titles mismatch.")
        exit()

    songs = []

    for x in range(0, len(artists)):
        song = {
            "artist": artists[x],
            "title": titles[x]
        }
        songs.append(song)

    return songs