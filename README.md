# Shuffle
This repository contains code for a Discord bot that displays a random or popular song daily or upon request.

The goal of the bot is to provide top and random songs at the ease of the user.

Uses [SpotifyCharts](https://spotifycharts.com/regional) and [TikTometer](https://tiktometer.com/) for the retrieval of the current top songs.

The **Shuffle** bot can be setup and deployed onto a stand alone system or onto Heroku if desired.

The **Shuffle** Bot can be deployed under their free tier of Heroku if desired.

Use the invitation link to invite the Shuffle bot into your server
  - [Shuffle Bot Invitation Link](https://discord.com/api/oauth2/authorize?client_id=745448751287631996&permissions=268954640&scope=bot)

## Quick Links:
- [Project Requirements](#project-requirements)
- [Optional Setup](#optional-setup)
- [Bot Permission Requirements](#bot-permission-requirements)
- [Stand-Alone Project Setup](#stand-alone-project-setup)
- [Docker Setup](#docker-setup)
- [Heroku Setup](#heroku-setup)
- [Heroku Deployment](#heroku-deployment)
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

## Optional Setup
- Heroku CLI
  - [Heroku CLI Installation Guide](https://devcenter.heroku.com/articles/heroku-cli)
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
- Follow the steps indicated above in [Stand-Alone Project Setup](stand-alone-project-setup) to get the base project setup
- Navigate to the project base directory
- Execute the following command to build the Docker image
  - **docker build -t shuffle .**
- Execute the following command to run the Docker container
  - **docker run -it shuffle**

## Heroku Setup
- Clone the repository
- Verify Heroku app has been created within Heroku dashboard
- Verify you're logged into your Heroku account within your terminal of choice
  - Execute **heroku login**
- Setup Heroku remote branch
  - Execute **heroku git:remote -a _name-of-app_**
- Push repository onto Heroku branch
  - Execute **git push heroku master**
  - Heroku will build the app each time a SCM change occurs
- Follow the [Heroku Config Var Setup Guide](https://devcenter.heroku.com/articles/config-vars) to add the following environment variables by adding it as a **Config Var** within the Heroku dashboard or through the Heroku CLI
  - **DISCORD_BOT_TOKEN**=***Shuffle bot secret token***
  - **DISCORD_BOT_TRIGGER**=**shuffle**

## Heroku Deployment
- Verify Heroku is setup in you machine
  - Run through steps indicated in [Heroku Setup](#heroku-setup)
- After commiting changes made locally, push onto the Heroku branch
  - Execute **git push heroku master**
  - Heroku will build the app each time a SCM change occurs
- Changes pushed onto Heroku branch will not be transferred onto **Shuffle** repository unless pushed onto repository as well

## Usage
- To bring up the **Shuffle Bot** help menu
  - **!shuffle help**
- To request a random song
  - **!shuffle**
- To request the current top song (US and Global)
  - **!shuffle top**
- To request the current top song on TikTok
  - **!shuffle tiktok**