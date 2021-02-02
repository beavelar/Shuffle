import time
import logging
from util.rest.rest import get_top_song
from util.rest.rest import get_tiktok_song
from util.rest.rest import get_random_song
from util.shuffle.ShuffleEnum import ShuffleEnum
from util.discord.discord_imp import sendMessage
from util.discord.ActionEnum import ActionEnum

logger = logging.getLogger(__name__)

#########################################################################################################

async def help(user, channel, help) -> None:
    '''
    Displays a help menu message onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel
    
    help : str
    '''

    await sendMessage(user, channel, help, False)

#########################################################################################################

async def top(user, channel, web) -> None:
    '''
    Displays the current top regional song (Global/US) onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel

    web : Dict -> { protocol: str, hostname: str, port: str }
    '''

    start = time.perf_counter()
    topUs, topGlobal = get_top_song(protocol=web.get('protocol'), hostname=web.get('hostname'), port=web.get('port'))
    report = topUs.generateTopSongReport() + '\n\n' + topGlobal.generateTopSongReport()
    stop = time.perf_counter()
    elapsedTime = stop - start
    logger.info(f'Top Song Report Retrieval Took: {elapsedTime} seconds')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'User: {user.display_name}')
    await sendMessage(user, channel, report, False)

#########################################################################################################

async def tiktok(user, channel, web) -> None:
    '''
    Displays the current top TikTok song onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel

    web : Dict -> { protocol: str, hostname: str, port: str }
    '''

    start = time.perf_counter()
    tiktokSong = get_tiktok_song(protocol=web.get('protocol'), hostname=web.get('hostname'), port=web.get('port'))
    report = tiktokSong.generateTopSongReport()
    stop = time.perf_counter()
    elapsedTime = stop - start
    logger.info(f'Top TikTok Song Report Retrieval Took: {elapsedTime} seconds')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'User: {user.display_name}')
    await sendMessage(user, channel, report, False)

#########################################################################################################

async def random(user, channel, web) -> None:
    '''
    Displays a random song (compiled from top songs) onto the desired Discord channel

    ...

    Arguments
    ----------
    user : discord.User
    
    channel : discord.Channel
    
    web : Dict -> { protocol: str, hostname: str, port: str }
    '''

    random = get_random_song(protocol=web.get('protocol'), hostname=web.get('hostname'), port=web.get('port'))
    await sendMessage(user, channel, random.generateRandomSongReport(), False)

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

    web : Dict -> { protocol: str, hostname: str, port: str }
    
    help : str
    '''

    if ShuffleEnum.CASE in args and ShuffleEnum.USER in args and ShuffleEnum.CHANNEL:
        if args.get('case') == ActionEnum.HELP:
            if ShuffleEnum.HELP in args:
                await help(args.get('user'), args.get('channel'), args.get('help'))
            else:
                logger.warning('Help menu not provided, ignoring function call')
        elif ShuffleEnum.WEB in args:
            if args.get('case') == ActionEnum.TOP:
                await top(args.get('user'), args.get('channel'), args.get('web'))
            elif args.get('case') == ActionEnum.TIKTOK:
                await tiktok(args.get('user'), args.get('channel'), args.get('web'))
            elif args.get('case') == ActionEnum.RANDOM:
                await random(args.get('user'), args.get('channel'), args.get('web'))
    else:
        logger.warning('Case, user or channel not provided, ignoring function call')