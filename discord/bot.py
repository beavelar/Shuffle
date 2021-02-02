import os
import aiocron
import logging
from dotenv import load_dotenv
from discord.ext import commands
from util.discord.ActionEnum import ActionEnum
from util.discord.discord_imp import createChannels
from util.shuffle.shuffle_case import shuffle_case

#########################################################################################################
# Global definitions

logging.basicConfig(format='%(levelname)s: %(asctime)s - %(name)s.%(funcName)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try: 
    helpMenuFile = open('support/help_menu.txt', 'r')
    welcomeFile = open('support/welcome_message.txt', 'r')
except Exception as ex:
    logger.critical('Exception caught attempting to open support files. Please verify support files exist and are in the correct location')
    logger.critical(str(ex))
    exit(1)

try:
    HELP_MENU = helpMenuFile.read()
    WELCOME_MESSAGE = welcomeFile.read()
except Exception as ex:
    logger.critical('Exception caught attempting to read support files')
    logger.critical(str(ex))
    exit(1)

try:
    load_dotenv()
    BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    BOT_TRIGGER = os.getenv('DISCORD_BOT_TRIGGER')

    WEB_SCRAPER_SETTINGS = {
        'protocol': os.getenv('WEB_SCRAPER_PROTOCOL'),
        'hostname': os.getenv('WEB_SCRAPER_HOSTNAME'),
        'port': os.getenv('WEB_SCRAPER_PORT')
    }
except Exception as ex:
    logger.critical('Failed to retrieve environment variables. Please verify environment variable exists')
    logger.critical(str(ex))
    exit(1)

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

#########################################################################################################
# Generates random song everyday at 17:00 UTC

@aiocron.crontab('0 17 * * *')
async def dailyRandomSong():
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.category != None and channel.category.name == 'Bots' and channel.name == 'shuffle':
                await shuffle_case(case=ActionEnum.RANDOM, user=bot.user, channel=channel, web=WEB_SCRAPER_SETTINGS)

#########################################################################################################
# Bot trigger command handler - Discord function that executes after bot command is received
#
# Parameters
# message: Message (Discord API)

@bot.command(name=BOT_TRIGGER)
async def random(message, *args):
    if (len(args) == 0):
        await shuffle_case(case=ActionEnum.RANDOM, user=bot.user, channel=message.channel, web=WEB_SCRAPER_SETTINGS)

    if (ActionEnum.TOP in args):
        await shuffle_case(case=ActionEnum.TOP, user=bot.user, channel=message.channel, web=WEB_SCRAPER_SETTINGS)
    
    if (ActionEnum.TIKTOK in args):
        await shuffle_case(case=ActionEnum.TIKTOK, user=bot.user, channel=message.channel, web=WEB_SCRAPER_SETTINGS)

    if (ActionEnum.HELP in args):
        await shuffle_case(case=ActionEnum.HELP, user=bot.user, channel=message.channel, web=WEB_SCRAPER_SETTINGS, help=HELP_MENU)

#########################################################################################################
# On_ready handler - Executes after bot starts up

@bot.event
async def on_ready():
    logger.info(f'{bot.user} has connected')
    await createChannels(bot.guilds, bot.user, 'Bots', 'shuffle', WELCOME_MESSAGE)

#########################################################################################################
# On_ready handler - Executes after bot starts up

@bot.event
async def on_guild_join(guild):
    logger.info(f'{bot.user} has joined a guild: {guild.name}')
    await createChannels([guild], bot.user, 'Bots', 'shuffle', WELCOME_MESSAGE)

#########################################################################################################
# On_error handler - Executes after unhandled errors pop up

@bot.event
async def on_error(event, *args, **kwargs):
    message = args[0]
    logger.error('Unhandled error occurred in on_error')
    logger.error(f'{message}')

#########################################################################################################
# On_command_error handler - Executes after unhandled errors pop up

@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.errors.CommandNotFound):
        logger.error('Unhandled error occurred in on_command_error')
        logger.error(str(error))

#########################################################################################################
# Startup command to start the bot

bot.run(BOT_TOKEN)