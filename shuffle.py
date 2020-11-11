import os
from dotenv import load_dotenv

from shuffle_util.shuffle_case import *

import discord
from discord.ext import tasks
from discord_util.DiscordMsgType import DiscordMsgType

#########################################################################################################
# Global definitions

channels = []

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
    BOT_TRIGGER = os.getenv('DISCORD_BOT_TRIGGER')
except Exception as ex:
    print('Failed to retrieving environment variables')
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
    # Hacky way of keeping channels persisted within Heroku's tool
    if not message.channel in channels:
        channels.append(message.channel)

    # Message isn't from Shuffle bot and message includes !shuffle trigger
    if (client.user != message.author) and (BOT_TRIGGER in message.content):
        if (DiscordMsgType.HELP in message.content):
            await shuffle_case(DiscordMsgType.HELP, client.user, message.channel, HELP_MENU)

        elif (DiscordMsgType.TOP in message.content):
            await shuffle_case(DiscordMsgType.TOP, client.user, message.channel, HELP_MENU)        
        
        elif (DiscordMsgType.TIKTOK in message.content):
            await shuffle_case(DiscordMsgType.TIKTOK, client.user, message.channel, HELP_MENU)
        
        else:
            await shuffle_case(DiscordMsgType.RANDOM, client.user, message.channel, HELP_MENU)
            
#########################################################################################################
# Discord task loop handler - Executes once daily

@tasks.loop(hours = 24)
async def dailyRandomSong():
    if len(channels) != 0:

        for channel in channels:
            await shuffle_case(DiscordMsgType.RANDOM, client.user, channel, HELP_MENU)

#########################################################################################################
# dailyRandomSong loop handler - Waits for Discord bot to be in a ready state

@dailyRandomSong.before_loop
async def before():
    await client.wait_until_ready()
    print(f'{client.user} is in a ready state')

#########################################################################################################
# On_ready handler - Executes after bot starts up

@client.event
async def on_ready():
    print(f'{client.user} has connected')

#########################################################################################################
# Startup command to start the bot

dailyRandomSong.start()
client.run(BOT_TOKEN)