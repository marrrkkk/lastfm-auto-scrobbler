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
5. Replace the song from `config.json` file

## Usage
1. Run the script with `python main.py`.
2. The script will automatically scrobble your track from the config.

## Hosting Options

To keep the Last.fm Auto-Scrobbler running continuously, consider deploying it on a cloud server or a hosting service. Some popular options include:

- **Heroku**: A platform-as-a-service that offers a free tier suitable for small projects.

- **AWS EC2**: Amazon's Elastic Compute Cloud provides scalable virtual servers.

- **Google Cloud**: Offers Compute Engine for hosting applications.

- **DigitalOcean**: Provides simple and cost-effective cloud hosting solutions.

Ensure your chosen hosting platform supports Python and allows you to run long-lived processes.

Remember to configure the necessary environment variables and any additional settings required for your chosen hosting platform.


## Important
Lastfm API has a limit of 2800 scrobbles per day and 5 request per second, therefore should not exceed to avoid getting rate limited.