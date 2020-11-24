import os
from dotenv import load_dotenv

from shuffle_util.shuffle_case import *

import discord
from discord.ext import tasks, commands
from discord_util.DiscordMsgType import DiscordMsgType

#########################################################################################################
# Global definitions

try: 
    helpMenuFile = open('support/help_menu.txt', 'r')
    welcomeFile = open('support/welcome_message.txt', 'r')
except Exception as ex:
    print('Exception caught attempting to open support files')
    print('Please verify support files exist and are in the correct location')
    print('Exiting..')
    print(str(ex))
    exit(1)

try:
    HELP_MENU = helpMenuFile.read()
    WELCOME_MESSAGE = welcomeFile.read()
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

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

#########################################################################################################
# Bot trigger command handler - Discord function that executes after bot command is received
#
# Parameters
# message: Message (Discord API)

@bot.command(name=BOT_TRIGGER)
async def random(message, *args):
    if (len(args) == 0):
        await shuffle_case(DiscordMsgType.RANDOM, bot.user, message.channel, HELP_MENU)

    if (DiscordMsgType.TOP in args):
        await shuffle_case(DiscordMsgType.TOP, bot.user, message.channel, HELP_MENU)
    
    if (DiscordMsgType.TIKTOK in args):
        await shuffle_case(DiscordMsgType.TIKTOK, bot.user, message.channel, HELP_MENU)

    if (DiscordMsgType.HELP in args):
        await shuffle_case(DiscordMsgType.HELP, bot.user, message.channel, HELP_MENU)
            
#########################################################################################################
# Discord task loop handler - Executes once daily

@tasks.loop(hours = 24)
async def dailyRandomSong():
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.category != None and channel.category.name == 'Bots' and channel.name == 'shuffle':
                await shuffle_case(DiscordMsgType.RANDOM, bot.user, channel, HELP_MENU)

#########################################################################################################
# dailyRandomSong loop handler - Waits for Discord bot to be in a ready state

@dailyRandomSong.before_loop
async def before():
    await bot.wait_until_ready()
    print(f'{bot.user} is in a ready state')

#########################################################################################################
# On_ready handler - Executes after bot starts up

@bot.event
async def on_ready():
    await createChannels(bot.guilds, bot.user, 'Bots', 'shuffle', WELCOME_MESSAGE)
    print(f'{bot.user} has connected')

#########################################################################################################
# Startup command to start the bot

dailyRandomSong.start()
bot.run(BOT_TOKEN)