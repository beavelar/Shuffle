# Discord Bot Implementation
This directory contains the code implementation for the **Discord** side of the **Shuffle** Discord bot.

Invite **Shuffle** into your **Discord** server using the invatation [link](https://discord.com/api/oauth2/authorize?client_id=745448751287631996&permissions=268528656&scope=bot)

## Quick Links:
- [Requirements](#requirements)
- [Bot Permission Requirements](#bot-permission-requirements)
- [Setup](#setup)
- [Startup](#startup)

----------------------------------

## Requirements
- Python
  - [Python Organization Website](https://www.python.org/)
- Python Libraries
  - Discord.py: [Discord.py Installation Guide](https://discordpy.readthedocs.io/en/latest/intro.html)
  - Dotenv: [Dotenv Installation Guide](https://pypi.org/project/python-dotenv/)
  - Requests: [Requests Installation Guide](https://pypi.org/project/requests/)
  - BeautifulSoup4: [BeautifulSoup4 Installation Guide](https://pypi.org/project/beautifulsoup4/)
  - Aiocron: [Aiocron Installation Guide](https://pypi.org/project/aiocron/)

To install the required libraries using the requirements.txt file, execute the following command:
- ***pip install -r requirements.txt***

## Bot Permission Requirements
The following are permission requirements needed by the **Shuffle** bot
 - **General Permissions**
   - Manage Roles
   - Manage Channels
   - View Channels
 - **Text Permissions**
   - Send Messages
   - Manage Messages
   - Embed Links
   - Read Message History

## Setup
- Navigate to the ***Shuffle/discord*** directory
- Create a **.env** file
  - Use the **.env.template** file as a template
- Create a **Discord** bot account
  - [Creating a Bot Account Guide](https://discordpy.readthedocs.io/en/latest/discord.html#)
- Invite the **Discord** bot into your **Discord** server with proper permissions
  - [Inviting Your Bot Guide](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot)
  - View [Bot Permission Requirements](#bot-permission-requirements) for the required permissions
- Retrieve bot secret token
  - In Discord developer page, navigate to "Bot"
  
    ![Discord Bot Selection](/images/bot-selection-snap.PNG)
  - Under **Token**, reveal the token by clicking on the **Click to Reveal Token** link

    ![Token Reveal](/images/token-reveal-snap.PNG)
- In the **.env** file, modify the following fields
  - **DISCORD_BOT_TOKEN**=***Shuffle bot secret token***
  - **DISCORD_BOT_TRIGGER**=**shuffle**

## Startup
- Navigate to the ***Shuffle/discord*** directory
- Execute the following command to start up the bot:
  - **python shuffle.py**
- View logs and verify no startup errors appears
- View Discord server and verify **Shuffle Bot** appears online