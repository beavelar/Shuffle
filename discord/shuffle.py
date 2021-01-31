import os
import aiocron
from dotenv import load_dotenv
from discord.ext import commands
from util.discord.discord_imp import createChannels
from util.discord.DiscordMsgType import DiscordMsgType
from util.shuffle.shuffle_case import shuffle_case
from util.shuffle.cache import buildRandomCache, buildTopSongCache, buildTopSongTikTokCache

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

RANDOM_SONG_CACHE = []
TOP_SONG_US_CACHE = None
TOP_SONG_GLOBAL_CACHE = None
TOP_SONG_TIKTOK_CACHE = None
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

#########################################################################################################
# Generates random song everyday at 17:00 UTC

@aiocron.crontab('0 17 * * *')
async def dailyRandomSong():
    global RANDOM_SONG_CACHE
    global TOP_SONG_US_CACHE
    global TOP_SONG_GLOBAL_CACHE
    global TOP_SONG_TIKTOK_CACHE

    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.category != None and channel.category.name == 'Bots' and channel.name == 'shuffle':
                await shuffle_case(DiscordMsgType.RANDOM, bot.user, channel, RANDOM_SONG_CACHE, TOP_SONG_US_CACHE, TOP_SONG_GLOBAL_CACHE, TOP_SONG_TIKTOK_CACHE, HELP_MENU)

#########################################################################################################
# Generates random song cache daily

@aiocron.crontab('0 0 */1 * *')
async def randomSongCache():
    global RANDOM_SONG_CACHE

    RANDOM_SONG_CACHE = await buildRandomCache()

#########################################################################################################
# Generates random song cache hourly

@aiocron.crontab('0 */1 * * *')
async def topSongCache():
    global TOP_SONG_US_CACHE
    global TOP_SONG_GLOBAL_CACHE
    global TOP_SONG_TIKTOK_CACHE

    try:
        TOP_SONG_TIKTOK_CACHE = await buildTopSongTikTokCache()
        TOP_SONG_US_CACHE = await buildTopSongCache('regional', 'us')
        TOP_SONG_GLOBAL_CACHE = await buildTopSongCache('regional', 'global')
    except Exception as ex:
        print('Unknown exception caught building cache at cron job')
        print(str(ex))

#########################################################################################################
# Bot trigger command handler - Discord function that executes after bot command is received
#
# Parameters
# message: Message (Discord API)

@bot.command(name=BOT_TRIGGER)
async def random(message, *args):
    global RANDOM_SONG_CACHE
    global TOP_SONG_US_CACHE
    global TOP_SONG_GLOBAL_CACHE
    global TOP_SONG_TIKTOK_CACHE

    if (len(args) == 0):
        await shuffle_case(DiscordMsgType.RANDOM, bot.user, message.channel, RANDOM_SONG_CACHE, TOP_SONG_US_CACHE, TOP_SONG_GLOBAL_CACHE, TOP_SONG_TIKTOK_CACHE, HELP_MENU)

    if (DiscordMsgType.TOP in args):
        await shuffle_case(DiscordMsgType.TOP, bot.user, message.channel, RANDOM_SONG_CACHE, TOP_SONG_US_CACHE, TOP_SONG_GLOBAL_CACHE, TOP_SONG_TIKTOK_CACHE, HELP_MENU)
    
    if (DiscordMsgType.TIKTOK in args):
        await shuffle_case(DiscordMsgType.TIKTOK, bot.user, message.channel, RANDOM_SONG_CACHE, TOP_SONG_US_CACHE, TOP_SONG_GLOBAL_CACHE, TOP_SONG_TIKTOK_CACHE, HELP_MENU)

    if (DiscordMsgType.HELP in args):
        await shuffle_case(DiscordMsgType.HELP, bot.user, message.channel, RANDOM_SONG_CACHE, TOP_SONG_US_CACHE, TOP_SONG_GLOBAL_CACHE, TOP_SONG_TIKTOK_CACHE, HELP_MENU)

#########################################################################################################
# On_ready handler - Executes after bot starts up

@bot.event
async def on_ready():
    global RANDOM_SONG_CACHE
    global TOP_SONG_US_CACHE
    global TOP_SONG_GLOBAL_CACHE
    global TOP_SONG_TIKTOK_CACHE

    try:
        RANDOM_SONG_CACHE = await buildRandomCache()
        TOP_SONG_TIKTOK_CACHE = await buildTopSongTikTokCache()
        TOP_SONG_US_CACHE = await buildTopSongCache('regional', 'us')
        TOP_SONG_GLOBAL_CACHE = await buildTopSongCache('regional', 'global')
    except Exception as ex:
        print('Unknown exception caught building cache at startup')
        print(str(ex))

    print(f'{bot.user} has connected')
    await createChannels(bot.guilds, bot.user, 'Bots', 'shuffle', WELCOME_MESSAGE)

#########################################################################################################
# On_ready handler - Executes after bot starts up

@bot.event
async def on_guild_join(guild):
    print(f'{bot.user} has joined a guild: {guild.name}')
    await createChannels([guild], bot.user, 'Bots', 'shuffle', WELCOME_MESSAGE)

#########################################################################################################
# On_error handler - Executes after unhandled errors pop up

@bot.event
async def on_error(event, *args, **kwargs):
    message = args[0]

    print('-----------------------------------------------------------------------------')
    print('Unhandled error occurred in on_error')
    print(f'Error: {message}')
    print('-----------------------------------------------------------------------------')

#########################################################################################################
# On_command_error handler - Executes after unhandled errors pop up

@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.errors.CommandNotFound):
        print('-----------------------------------------------------------------------------')
        print('Unhandled error occurred in on_command_error')
        print(str(error))
        print('-----------------------------------------------------------------------------')

#########################################################################################################
# Startup command to start the bot

bot.run(BOT_TOKEN)