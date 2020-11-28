import time

from shuffle_util.thread import Thread
from shuffle_util.request import Request

#########################################################################################################
# Displays a help menu message onto the desired Discord channel
#
# Returns: List of Song

async def buildRandomCache():
    print('-----------------------------------------------------------------------------')
    print(f'Building song cache')
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
    print(f'Song Cache Building Took: {elapsedTime} seconds')
    print('-----------------------------------------------------------------------------\n')

    return randomSongCache