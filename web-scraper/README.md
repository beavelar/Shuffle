# Web-Scraper Implementation
This directory contains the code implementation for the **Web-Scraper** side of the **Shuffle** Discord bot.

Invite **Shuffle** into your **Discord** server using the invatation [link](https://discord.com/api/oauth2/authorize?client_id=745448751287631996&permissions=268528656&scope=bot)

Uses [SpotifyCharts](https://spotifycharts.com/regional) and [Tokboard](https://tokboard.com/) for the retrieval of the current top songs.

## Quick Links:
- [Requirements](#requirements)
- [Setup](#setup)
- [Startup](#startup)

----------------------------------

## Requirements
- Python
  - [Python Organization Website](https://www.python.org/)
- Python Libraries
  - Dotenv: [Dotenv Installation Guide](https://pypi.org/project/python-dotenv/)
  - Requests: [Requests Installation Guide](https://pypi.org/project/requests/)
  - BeautifulSoup4: [BeautifulSoup4 Installation Guide](https://pypi.org/project/beautifulsoup4/)
  - Aiocron: [Aiocron Installation Guide](https://pypi.org/project/aiocron/)

To install the required libraries using the requirements.txt file, execute the following command:
- ***pip install -r requirements.txt***

## Setup
- Navigate to the ***Shuffle/web-scraper*** directory
- Create a **.env** file
  - Use the **.env.template** file as a template
- In the **.env** file, modify the following fields
  - **WEB_SCRAPER_HOSTNAME**=***Web-scraper hostname***
  - **WEB_SCRAPER_PORT**=***Web-scraper port***

## Startup
- Navigate to the ***Shuffle/web-scraper*** directory
- Execute the following command to start up the bot:
  - **python server.py**
- View logs and verify no startup errors appears