import discord
from discord_util.discord_imp import *

#########################################################################################################
# Global definitions

MOCK_TRIGGER = '!song'

try: 
    tokenFile = open('environment/.env', 'r')
    helpMenuFile = open('environment/help_menu.txt', 'r')
except Exception as ex:
    print('Exception caught attempting to open environment files')
    print('Please verify .env file exist and is in the correct location')
    print('Exiting..')
    print(str(ex))
    exit(1)

try:
    BOT_TOKEN = tokenFile.read()
    HELP_MENU = helpMenuFile.read()
except Exception as ex:
    print('Exception caught attempting to read environment files')
    print('Exiting..')
    print(str(ex))
    exit(1)

client = discord.Client()

#########################################################################################################
# On_message handler - Discord function that executes after message is detected from Discord server
#
# Parameters
# message: Message (Discord API)

@client.event
async def on_message(message):
    # Message isn't from Shuffle bot and message includes !song trigger
    if (client.user != message.author) and (MOCK_TRIGGER in message.content):
        if ('help' in message.content):
            await sendMessage(client.user, message.channel, HELP_MENU)

#########################################################################################################
# On_ready handler - Executes after bot starts up

@client.event
async def on_ready():
    print(f'{client.user} has connected')

#########################################################################################################
# Startup command to start the bot

client.run(BOT_TOKEN)