# Shuffle
This repository contains code for a Discord bot that displays a random or popular song daily or upon request.

The goal of the bot is to provide a random song at the ease of the user.

The **Shuffle** bot can be setup and deployed onto a stand alone system or onto Heroku if desired.

The **Shuffle** Bot can be deployed under their free tier of Heroku if desired.

## Quick Links:
- [Project Requirements](#project-requirements)
- [Bot Permission Requirements](#bot-permission-requirements)
- [Heroku Setup](#heroku-setup)
- [Heroku Deployment](#heroku-deployment)
- [Stand-Alone Project Setup](#stand-alone-project-setup)
- [Usage](#usage)

----------------------------------

## Project Requirements
- Python
  - [Python Organization Website](https://www.python.org/)
- Discord library
  - [Discord.py Installation Guide](https://discordpy.readthedocs.io/en/latest/intro.html)
- Dotenv library
  - [Dotenv Installation Guide](https://pypi.org/project/python-dotenv/)
- Heroku CLI
  - [Heroku CLI Installation Guide](https://devcenter.heroku.com/articles/heroku-cli)

## Bot Permission Requirements
The following are permission requirements needed by the MoCk BoT
 - **General Permissions**
   - View Channels
 - **Text Permissions**
   - Send Messages
   - Manage Messages
   - Embed Links
   - Attach Files
   - Read Message History
   - Mention everyone
   - Use External Emojis

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
- Add ***DISCORD_BOT_TOKEN*** as an environment variable by adding it as a **Config Var** within the Heroku dashboard or through the Heroku CLI
  - [Heroku Config Var Setup Guide](https://devcenter.heroku.com/articles/config-vars)
  - Set the value of the ***DISCORD_BOT_TOKEN*** variable to be the **Shuffle** bot secret token

## Heroku Deployment
- Verify Heroku is setup in you machine
  - Run through steps indicated in [Heroku Setup](#heroku-setup)
- After commiting changes made locally, push onto the Heroku branch
  - Execute **git push heroku master**
  - Heroku will build the app each time a SCM change occurs
- Changes pushed onto Heroku branch will not be transferred onto **Shuffle** repository unless pushed onto repository as well

## Stand-Alone Project Setup
- Clone the repository
- Create Discord bot account
  - [Creating a Bot Account Guide](https://discordpy.readthedocs.io/en/latest/discord.html#)
- Invite Discord bot into your Discord server with proper permissions
  - [Inviting Your Bot Guide](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot)
  - View [Bot Permission Requirements](#bot-permission-requirements) for the required permissions  
- After cloning the repository, you should have a **Shuffle** directory, navigate to the **Shuffle** directory and create an empty .env file
  - This will contain our bot secret token
- Retrieve bot secret token
  - In Discord developer page, navigate to "Bot"
  
    ![Discord Bot Selection](/images/bot-selection-snap.PNG)
  - Under "Token", reveal token by clicking on the "Click to Reveal Token" link

    ![Token Reveal](/images/token-reveal-snap.PNG)
- In the .env file, create a **DISCORD_BOT_TOKEN** entry with the value being the Discord bot token
  - Ex. **DISCORD_BOT_TOKEN=_SECRET TOKEN_**
- Open a command line window of choice
  - Command prompt, GitBash, etc.
- Navigate to the project base directory
- Execute the following command to spin up the bot:
  - **python shuffle.py**
- View Discord server
  - **Shuffle Bot** should now appear as online and listening to channel messages

## Usage
- To bring up the **Shuffle Bot** help menu
  - **!song help**
- To request a random song
  - **!song**
- To request a random song (Genre specific)
  - **!song _genre_**
  - Ex. **!song hip hop**
- To request the current top song on TikTok
  - **!song tiktok**
- To request the current top song (Genre specific)
  - **!song top _genre_**
  - Ex. **!song top hip hop**