import os
import time
import json
import aiocron
import asyncio
import logging
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer
from util.web.cache import buildRandomCache, buildTopSongCache, buildTopSongTikTokCache

#########################################################################################################
# Global definitions

logging.basicConfig(format='%(levelname)s: %(asctime)s - %(name)s.%(funcName)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    load_dotenv()
    HOSTNAME = os.getenv('WEB_SCRAPER_HOSTNAME')
    PORT = os.getenv('WEB_SCRAPER_PORT')
except Exception as ex:
    logger.critical('Failed to retrieve environment variables. Please verify environment variable exists')
    logger.critical(str(ex))
    exit(1)

RANDOM_SONG_CACHE = []
TOP_SONG_US_CACHE = None
TOP_SONG_GLOBAL_CACHE = None
TOP_SONG_TIKTOK_CACHE = None

#########################################################################################################
# Server class

class Server(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self.set_headers()

    def do_GET(self):
        logger.info(f'Received GET request - Path: {self.path}')
        self.set_headers()

        if 'get_random_song' in self.path:
            logger.info('Random')
        elif 'get_top_song' in self.path:
            logger.info('Top')
        elif 'get_tiktok_song' in self.path:
            logger.info('TikTok')
        
        response = json.dumps({'hello': 'world', 'received': 'ok'})
        logger.info(f'Response: {response}')
        self.wfile.write(response.encode('utf-8'))

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
        logger.error('Unknown exception caught building cache at cron job')
        logger.error(str(ex))

#########################################################################################################
# Builds random and top songs cache

async def buildSongCache():
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
        logger.error('Unknown exception caught building cache at startup')
        logger.error(str(ex))

#########################################################################################################
# Server startup handler

async def run():
    server = HTTPServer((HOSTNAME, int(PORT)), Server)
    logger.info('Server is up and listening')
    logger.info(f'Port: {PORT}')
    await buildSongCache()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    logger.info('Server stopped')

#########################################################################################################
# Server startup

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = [loop.create_task(run())]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()