import time
import random as rand

from shuffle_util.thread import *
from shuffle_util.request import *

from spotify_util.Song import *
from spotify_util.spotify_util import *

from discord_util.discord_imp import *

from tiktometer_util.Song import *
from tiktometer_util.tiktometer_util import *

from discord_util.DiscordMsgType import DiscordMsgType

#########################################################################################################
# Displays a help menu message onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)
# helpMenu: string

async def help(user, channel, helpMenu):
    await sendMessage(user, channel, helpMenu, False)

#########################################################################################################
# Displays the current top regional song (Global/US) onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)

async def top(user, channel):
    start = time.perf_counter()

    topGlobalSong = getTopSong('regional', 'global')
    topUSSong = getTopSong('regional', 'us')
    report = topGlobalSong.generateTopSongReport() + '\n\n' + topUSSong.generateTopSongReport()
    
    stop = time.perf_counter()
    elapsedTime = stop - start

    print('-----------------------------------------------------------------------------')
    print(f'Top Song Retrieval Took: {elapsedTime} seconds')
    print(f'Channel Name: {channel.name}')
    print(f'User: {user.display_name}')
    print('-----------------------------------------------------------------------------\n')

    await sendMessage(user, channel, report, False)

#########################################################################################################
# Displays the current top TikTok song onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)

async def tiktok(user, channel):
    start = time.perf_counter()

    topTikTokSong = getTopTikTokSong()
    report = topTikTokSong.generateTopSongReport()
    
    stop = time.perf_counter()
    elapsedTime = stop - start

    print('-----------------------------------------------------------------------------')
    print(f'Top Song Retrieval Took: {elapsedTime} seconds')
    print(f'Channel Name: {channel.name}')
    print(f'User: {user.display_name}')
    print('-----------------------------------------------------------------------------\n')

    await sendMessage(user, channel, report, False)

#########################################################################################################
# Displays a random song (compiled from top songs) onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)

async def random(user, channel):
    start = time.perf_counter()

    songs = []
    threads = []
    requestList = [Request('regional', 'us'), Request('regional', 'global'), Request('viral', 'us'), Request('viral', 'global')]
    threadList = ['RandomThread-1', 'RandomThread-2', 'RandomThread-3', 'RandomThread-4']

    for index in range(4):
        thread = Thread(threadList[index], requestList[index].getChart(), requestList[index].getRegion(), songs)
        thread.start()
        threads.append(thread)

    for thread in threads:
        # Waits for thread to complete
        thread.join()

    randomIndex = rand.randint(0, len(songs) - 1)
    randomSong = rand.randint(0, len(songs[randomIndex]) - 1)

    stop = time.perf_counter()
    elapsedTime = stop - start

    print('-----------------------------------------------------------------------------')
    print(f'Top Song Retrieval Took: {elapsedTime} seconds')
    print(f'Channel Name: {channel.name}')
    print(f'User: {user.display_name}')
    print('-----------------------------------------------------------------------------\n')

    await sendMessage(user, channel, songs[randomIndex][randomSong].generateRandomSongReport(), False)

#########################################################################################################
# Determines which case to execute (Basic switch/case implementation)
#
# Parameters
# case: DiscordMsgType enum value
# user: User (Discord API)
# channel: Channel (Discord API)
# helpMenu: string

async def shuffle_case(case, user, channel, helpMenu):
    if case == DiscordMsgType.HELP:
        await help(user, channel, helpMenu)
    elif case == DiscordMsgType.TOP:
        await top(user, channel)
    elif case == DiscordMsgType.TIKTOK:
        await tiktok(user, channel)
    elif case == DiscordMsgType.RANDOM:
        await random(user, channel)