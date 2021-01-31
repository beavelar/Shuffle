import time
import logging
from util.shuffle.thread import Thread
from util.shuffle.request import Request
from util.spotify.spotify_util import getTop200List
from util.tokboard.tokboard_util import getTopTikTokSong

logger = logging.getLogger(__name__)

#########################################################################################################
# Builds top song cache to be used when top command is executed
#
# Returns: Song

async def buildTopSongCache(urlExt, region):
    logger.info(f'Building top song cache for: {region}')
    start = time.perf_counter()
    top200 = getTop200List(urlExt, region)
    stop = time.perf_counter()
    elapsedTime = stop - start
    logger.info(f'Top song cache building for {region} took: {elapsedTime} seconds')
    return top200[0]

#########################################################################################################
# Builds top tiktok song cache to be used when tiktok command is executed
#
# Returns: Song

async def buildTopSongTikTokCache():
    logger.info(f'Building top TikTok song cache')
    start = time.perf_counter()
    topTikTokSong = getTopTikTokSong()
    stop = time.perf_counter()
    elapsedTime = stop - start
    logger.info(f'Top TikTok song cache building took: {elapsedTime} seconds')
    return topTikTokSong

#########################################################################################################
# Builds random song cache to be used when random command is executed
#
# Returns: List of Song

async def buildRandomCache():
    logger.info(f'Building random song cache')
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
    logger.info(f'Random song cache building took: {elapsedTime} seconds')
    return randomSongCache