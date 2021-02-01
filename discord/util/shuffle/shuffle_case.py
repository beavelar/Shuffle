import time
import logging
import random as rand
from util.shuffle.ShuffleEnum import ShuffleEnum
from util.discord.discord_imp import sendMessage
from util.discord.ActionEnum import ActionEnum

logger = logging.getLogger(__name__)

#########################################################################################################

async def help(user, channel, helpMenu) -> None:
    '''
    Displays a help menu message onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel
    
    helpMenu : str
    '''

    await sendMessage(user, channel, helpMenu, False)

#########################################################################################################

async def top(user, channel, topUs, topGlobal) -> None:
    '''
    Displays the current top regional song (Global/US) onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel

    topUs : Song

    topGlobal : Song
    '''

    start = time.perf_counter()
    report = topUs.generateTopSongReport() + '\n\n' + topGlobal.generateTopSongReport()
    stop = time.perf_counter()
    elapsedTime = stop - start
    logger.info(f'Top Song Report Retrieval Took: {elapsedTime} seconds')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'User: {user.display_name}')
    await sendMessage(user, channel, report, False)

#########################################################################################################

async def tiktok(user, channel, tiktokSong) -> None:
    '''
    Displays the current top TikTok song onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel

    tiktokSong : Song
    '''

    start = time.perf_counter()
    report = tiktokSong.generateTopSongReport()
    stop = time.perf_counter()
    elapsedTime = stop - start
    logger.info(f'Top TikTok Song Report Retrieval Took: {elapsedTime} seconds')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'User: {user.display_name}')
    await sendMessage(user, channel, report, False)

#########################################################################################################

async def random(user, channel, songs) -> None:
    '''
    Displays a random song (compiled from top songs) onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel
    
    songs : [Song]
    '''

    randomIndex = rand.randint(0, len(songs) - 1)
    randomSong = rand.randint(0, len(songs[randomIndex]) - 1)
    await sendMessage(user, channel, songs[randomIndex][randomSong].generateRandomSongReport(), False)

#########################################################################################################

async def shuffle_case(**args) -> None:
    '''
    Determines which case to execute (Basic switch/case implementation)

    ...

    Parameters
    ----------
    case : ActionEnum
    
    user : User (Discord API)
    
    channel : Channel (Discord API)
    
    songs : List of Song
    
    helpMenu : str
    '''

    if ShuffleEnum.CASE in args and ShuffleEnum.USER in args and ShuffleEnum.CHANNEL in args:
        if args.get('case') == ActionEnum.HELP:
            if ShuffleEnum.HELP in args:
                await help(args.get('user'), args.get('channel'), args.get('help'))
            else:
                logger.warning('Help menu not provided, ignoring function call')
        elif args.get('case') == ActionEnum.TOP:
            if ShuffleEnum.US_SONGS in args and ShuffleEnum.GLOBAL_SONGS in args:
                await top(args.get('user'), args.get('channel'), args.get('us_songs'), args.get('global_songs'))
            else:
                logger.warning('Top us or top global songs not provided, ignoring function call')
        elif args.get('case') == ActionEnum.TIKTOK:
            if ShuffleEnum.TIKTOK in args:
                await tiktok(args.get('user'), args.get('channel'), args.get('tiktok'))
            else:
                logger.warning('TikTok song not provided, ignoring function call')
        elif args.get('case') == ActionEnum.RANDOM:
            if ShuffleEnum.SONGS in args:
                await random(args.get('user'), args.get('channel'), args.get('songs'))
            else:
                logger.warning('Songs not provided, ignoring function call')
    else:
        logger.warning('Case, user or channel not provided, ignoring function call')