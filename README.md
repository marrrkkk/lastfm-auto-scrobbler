# Last.fm Auto-Scrobbler

## Overview
This Python script enables automatic scrobbling to Last.fm using the Last.fm API. Please be aware of Last.fm API rate limits to avoid any disruptions in service.

## Requirements
- Python
- Last.fm API account
- colorama (for console colors)
- dotenv (for environment variables)
- pylast (Last.fm API wrapper)

## Installation
1. Clone this repository.
2. Install the required dependencies using pip install -r requirements.txt.
3. Get you Lastfm API account at https://www.last.fm/api/account/create
4. Rename `.env.example` to `.env` file and add your Last.fm API credentials:
```
API_KEY=your_api_key
API_SECRET=your_api_secret
LASTFM_USERNAME=your_lastfm_username
LASTFM_PASSWORD=your_lastfm_password
```
5. Replace the song from `config.json` file, add scrobble limit (LIMIT) and interval between each scrobble (INTERVAL) in seconds.

## Usage
1. Run the script with `python main.py`.
2. The script will automatically scrobble your track from the config.

## Important
Lastfm API has a limit of 2800 scrobbles per day and 5 request per second, therefore should not exceed to avoid getting rate limited.
