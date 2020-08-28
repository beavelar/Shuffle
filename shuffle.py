import os
from dotenv import load_dotenv

import discord
from discord_util.discord_imp import *

from spotify_util.Song import *
from spotify_util.spotify_util import *

from tiktometer_util.Song import *
from tiktometer_util.tiktometer_util import *

#########################################################################################################
# Global definitions

MOCK_TRIGGER = '!shuffle'

try: 
    helpMenuFile = open('support/help_menu.txt', 'r')
except Exception as ex:
    print('Exception caught attempting to open support files')
    print('Please verify support files exist and are in the correct location')
    print('Exiting..')
    print(str(ex))
    exit(1)

try:
    HELP_MENU = helpMenuFile.read()
except Exception as ex:
    print('Exception caught attempting to read support files')
    print('Exiting..')
    print(str(ex))
    exit(1)

try:
    load_dotenv()
    BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
except Exception as ex:
    print('Failed to retrieve DISCORD_BOT_TOKEN environment variable')
    print('Please verify environment variable exists')
    print('Exiting..')
    exit(1)

client = discord.Client()

#########################################################################################################
# On_message handler - Discord function that executes after message is detected from Discord server
#
# Parameters
# message: Message (Discord API)

@client.event
async def on_message(message):
    # Message isn't from Shuffle bot and message includes !shuffle trigger
    if (client.user != message.author) and (MOCK_TRIGGER in message.content):
        if ('help' in message.content):
            await sendMessage(client.user, message.channel, HELP_MENU)
        elif ('top' in message.content):
            topGlobalSong = getTopSong('global', 'Global')
            topUSSong = getTopSong('us', 'US')
            report = topGlobalSong.generateReport('Top song') + '\n\n' + topUSSong.generateReport('Top song')
            
            await sendMessage(client.user, message.channel, report)
        elif ('tiktok' in message.content):
            topTikTokSong = getTopTikTokSong()
            
            await sendMessage(client.user, message.channel, topTikTokSong.generateReport())

#########################################################################################################
# On_ready handler - Executes after bot starts up

@client.event
async def on_ready():
    print(f'{client.user} has connected')

#########################################################################################################
# Startup command to start the bot

client.run(BOT_TOKEN)