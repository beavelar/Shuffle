import time

from shuffle_util.thread import Thread
from shuffle_util.request import Request

from spotify_util.spotify_util import getTop200List

from tokboard_util.tokboard_util import getTopTikTokSong

#########################################################################################################
# Builds top song cache to be used when top command is executed
#
# Returns: Song

async def buildTopSongCache(urlExt, region):
    print('-----------------------------------------------------------------------------')
    print(f'Building top song cache for: {region}')
    print('-----------------------------------------------------------------------------\n')

    start = time.perf_counter()
    top200 = getTop200List(urlExt, region)

    stop = time.perf_counter()
    elapsedTime = stop - start

    print('-----------------------------------------------------------------------------')
    print(f'Top song cache building for {region} took: {elapsedTime} seconds')
    print('-----------------------------------------------------------------------------\n')

    return top200[0]

#########################################################################################################
# Builds top tiktok song cache to be used when tiktok command is executed
#
# Returns: Song

async def buildTopSongTikTokCache():
    print('-----------------------------------------------------------------------------')
    print(f'Building top TikTok song cache')
    print('-----------------------------------------------------------------------------\n')

    start = time.perf_counter()
    topTikTokSong = getTopTikTokSong()

    stop = time.perf_counter()
    elapsedTime = stop - start

    print('-----------------------------------------------------------------------------')
    print(f'Top TikTok song cache building took: {elapsedTime} seconds')
    print('-----------------------------------------------------------------------------\n')

    return topTikTokSong

#########################################################################################################
# Builds random song cache to be used when random command is executed
#
# Returns: List of Song

async def buildRandomCache():
    print('-----------------------------------------------------------------------------')
    print(f'Building random song cache')
    print('-----------------------------------------------------------------------------\n')

    start = time.perf_counter()

    threads = []
    randomSongCache = []
    requestList = [Request('regional', 'us'), Request('regional', 'global'), Request('viral', 'us'), Request('viral', 'global')]
    threadList = ['RandomThread-1', 'RandomThread-2', 'RandomThread-3', 'RandomThread-4']

    for index in range(4):
        thread = Thread(threadList[index], requestList[index].getChart(), requestList[index].getRegion(), randomSongCache)
        thread.start()
        threads.append(thread)

    for thread in threads:
        # Waits for thread to complete
        thread.join()

    stop = time.perf_counter()
    elapsedTime = stop - start

    print('-----------------------------------------------------------------------------')
    print(f'Random song cache building took: {elapsedTime} seconds')
    print('-----------------------------------------------------------------------------\n')

    return randomSongCache