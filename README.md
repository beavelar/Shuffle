# Shuffle
This repository contains code for a Discord bot that displays a random song daily or upon request.

The goal of the bot is to provide a random song at the ease of the user.

The **Shuffle** bot can be setup and deployed onto a stand alone system or onto Heroku if desired.

The **Shuffle** Bot can be deployed under their free tier of Heroku if desired.

## Quick Links:
- [Project Requirements](#project-requirements)
- [Bot Permission Requirements](#bot-permission-requirements)
- [Heroku Setup](#heroku-setup)
- [Heroku Deployment](#heroku-deployment)

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
  - Execute *heroku login*
- Setup Heroku remote branch
  - Execute *heroku git:remote -a name-of-app*
- Push repository onto Heroku branch
  - Execute *git push heroku master*
  - Heroku will build the app each time a SCM change occurs
- Add *DISCORD_BOT_TOKEN* as an environment variable by adding it as a **Config Var** within the Heroku dashboard or through the Heroku CLI
  - [Heroku Config Var Setup Guide](https://devcenter.heroku.com/articles/config-vars)
  - Set the value of the *DISCORD_BOT_TOKEN* variable to be the **Shuffle** bot secret token

## Heroku Deployment
- Verify Heroku is setup in you machine
  - Run through steps indicated in [Heroku Setup](#heroku-setup)
- After commiting changes made locally, push onto the Heroku branch
  - Execute *git push heroku master*
  - Heroku will build the app each time a SCM change occurs
- Changes pushed onto Heroku branch will not be transferred onto **Shuffle** repository unless pushed onto repository as well