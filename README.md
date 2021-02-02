# Shuffle
This repository contains code for a **Discord** bot that displays a random or popular song daily or upon request.

The goal of the bot is to provide top and random songs at the ease of the user.

Invite **Shuffle** into your **Discord** server using the invatation [link](https://discord.com/api/oauth2/authorize?client_id=745448751287631996&permissions=268528656&scope=bot)

## Quick Links:
- [Requirements](#requirements)
- [Setup](#setup)
- [Startup](#startup)
- [Shutdown](#shutdown)
- [Usage](#usage)

----------------------------------

## Requirements
- Docker

View the ***discord*** [readme](/discord/README.md) and ***web-scraper*** [readme](/web-scraper/README.md) if not running through **Docker**

## Setup
- Clone the repository
- Navigate to the ***Shuffle*** directory
- Create a **.env** file
  - Use the **.env.template** file as a template
- In the **.env** file, modify the following fields
  - **WEB_SCRAPER_PROTOCOL**=***Web-scraper protocol***
  - **WEB_SCRAPER_PORT**=***Web-scraper port***
  - **WEB_SCRAPER_HOSTNAME**=***Web-scraper hostname***
- Follow the ***discord*** [setup](/discord/README.md#setup) steps
- Follow the ***web-scraper*** [setup](/web-scraper/README.md#setup) steps

## Startup
- Navigate to the ***Shuffle*** directory
- Execute the following command to build the **Docker** images and startup the containers
  - Interactive process: ***docker-compose up --build***
  - Detached from the process: ***docker-compose up -d --build***
- View logs and verify no startup errors appear

## Shutdown
- Navigate to the ***Shuffle*** directory
- Execute the following command to stop the **Docker** containers
  - ***docker-compose down***

## Usage
- To bring up the **Shuffle Bot** help menu
  - **!shuffle help**
- To request a random song
  - **!shuffle**
- To request the current top song (US and Global)
  - **!shuffle top**
- To request the current top song on TikTok
  - **!shuffle tiktok**