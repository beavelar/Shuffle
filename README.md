# Shuffle
This repository contains code for a Discord bot that displays a random or popular song daily or upon request.

The goal of the bot is to provide top and random songs at the ease of the user.

Uses [SpotifyCharts](https://spotifycharts.com/regional) and [TikTometer](https://tiktometer.com/) for the retrieval of the current top songs.

Use the invitation link to invite the Shuffle bot into your server
  - [Shuffle Bot Invitation Link](https://discord.com/api/oauth2/authorize?client_id=745448751287631996&permissions=268954640&scope=bot)

## Quick Links:
- [Project Requirements](#project-requirements)
- [Optional Setup](#optional-setup)
- [Bot Permission Requirements](#bot-permission-requirements)
- [Stand-Alone Project Setup](#stand-alone-project-setup)
- [Docker Setup](#docker-setup)
- [Usage](#usage)

----------------------------------

## Project Requirements
- Python
  - [Python Organization Website](https://www.python.org/)
- Discord Python library
  - [Discord.py Installation Guide](https://discordpy.readthedocs.io/en/latest/intro.html)
- Dotenv Python library
  - [Dotenv Installation Guide](https://pypi.org/project/python-dotenv/)
- Requests Python library
  - [Requests Installation Guide](https://pypi.org/project/requests/)
- BeautifulSoup4 Python library
  - [BeautifulSoup4 Installation Guide](https://pypi.org/project/beautifulsoup4/)

To install the required libraries using the requirements.txt file, execute the following command:
- ***pip install -r requirements.txt***

## Optional Setup
- Docker
  - [Docker Installation Guide](https://docs.docker.com/get-docker/)

## Bot Permission Requirements
The following are permission requirements needed by the Shuffle bot
 - **General Permissions**
   - Manage Roles
   - Manage Channels
   - View Channels
 - **Text Permissions**
   - Send Messages
   - Manage Messages
   - Embed Links
   - Attach Files
   - Read Message History
   - Mention everyone
   - Use External Emojis

## Stand-Alone Project Setup
- Clone the repository
- Create Discord bot account
  - [Creating a Bot Account Guide](https://discordpy.readthedocs.io/en/latest/discord.html#)
- Invite Discord bot into your Discord server with proper permissions
  - [Inviting Your Bot Guide](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot)
  - View [Bot Permission Requirements](#bot-permission-requirements) for the required permissions  
- After cloning the repository, you should have a **Shuffle** directory, navigate to the **Shuffle** directory and create an empty .env file
  - A .env template file is provided for ease of usage
  - This will contain our bot's environment variables
- Retrieve bot secret token
  - In Discord developer page, navigate to "Bot"
  
    ![Discord Bot Selection](/images/bot-selection-snap.PNG)
  - Under "Token", reveal token by clicking on the "Click to Reveal Token" link

    ![Token Reveal](/images/token-reveal-snap.PNG)
- Add the following environment variables in the .env file
  - **DISCORD_BOT_TOKEN**=***Shuffle bot secret token***
  - **DISCORD_BOT_TRIGGER**=**shuffle**
- Open a command line window of choice
  - Command prompt, GitBash, etc.
- Navigate to the project base directory
- Execute the following command to spin up the bot:
  - **python shuffle.py**
- View Discord server
  - **Shuffle Bot** should now appear as online and listening to channel messages

## Docker Setup
- Follow the steps indicated above in [Stand-Alone Project Setup](#stand-alone-project-setup) to get the base project setup
- Navigate to the project base directory
- Execute the following command to build the Docker image
  - **docker build -t shuffle .**
- Execute the following command to run the Docker container
  - Interactive process: **docker run -it shuffle**
  - Detached from the process: **docker run -d --rm shuffle**

## Usage
- To bring up the **Shuffle Bot** help menu
  - **!shuffle help**
- To request a random song
  - **!shuffle**
- To request the current top song (US and Global)
  - **!shuffle top**
- To request the current top song on TikTok
  - **!shuffle tiktok**