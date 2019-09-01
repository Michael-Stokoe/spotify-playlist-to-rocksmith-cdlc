# Spotify Playlist to Rocksmith DLC

This python script accepts a spotify playlist URL and then goes and logs into Customs Forge Ignition, searches for, and opens the download pages for all the songs in the playlist.

## Work in progress!

Currently the script only logs into CustomsForge and searches ignition for songs.

There is an example of how to call the script in the comments inside the scrapeIgnition.py file.

## Configuration

To use this you must have an account at CustomsForge.
Simply enter your credentials in the ignitionScraperTools.py file.

## Defining the search terms

Currently to use this you should add a line or two into scrapeIgnition.py:

### First line to add would be this:

```python    
    # Array of search term dictionaries...
    # Currently only artist and title are supported. This will likely not change.
    # You can define as many songs as you want here, the script will loop through this array.
    searches = [
        {
            'artist': 'muse',
            'title': 'exo politics'
        },
        {
            'artist': 'eric clapton',
            'title': 'cocaine'
        }
    ]
```

## TODO List:
_This list may expand over time, depending on which features I think of and decide to implement_

 - [ ] - Spotify playlist scraper
 - [ ] - Convert list of songs to array like above
 - [ ] - Final link-up of scrapers