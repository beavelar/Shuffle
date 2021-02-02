import logging
import requests
from util.spotify.Song import Song as spotify
from util.tokboard.Song import Song as tokboard

logger = logging.getLogger(__name__)

def get_top_song(protocol, hostname, port):
    '''
    Requests top song json data from web-scraper

    ...

    Arguments
    ----------
    protocol : str
    
    hostname : str

    port : str

    ...

    Returns
    ----------
    Song, Song
    '''

    logger.info(f'Requesting song from {hostname}: /get_top_song')
    url = f'{protocol}://{hostname}:{port}/get_top_song'
    response = requests.get(url)
    responseJson = response.json()
    logger.info(f'Response: {responseJson}')

    topUsJson = responseJson.get('us')
    topGlobalJson = responseJson.get('global')
    topUs = spotify(topUsJson.get('region'), topUsJson.get('title'), topUsJson.get('artist'), topUsJson.get('streams'))
    topGlobal = spotify(topGlobalJson.get('region'), topGlobalJson.get('title'), topGlobalJson.get('artist'), topGlobalJson.get('streams'))

    return topUs, topGlobal

def get_tiktok_song(protocol, hostname, port):
    '''
    Requests top tiktok song json data from web-scraper

    ...

    Arguments
    ----------
    protocol : str
    
    hostname : str

    port : str

    ...

    Returns
    ----------
    Song
    '''

    logger.info(f'Requesting song from {hostname}: /get_tiktok_song')
    url = f'{protocol}://{hostname}:{port}/get_tiktok_song'
    response = requests.get(url)
    responseJson = response.json()
    logger.info(f'Response: {responseJson}')

    tiktokJson = responseJson.get('tiktok')
    tiktok = tokboard(tiktokJson.get('title'), tiktokJson.get('artist'), tiktokJson.get('views'), tiktokJson.get('videos'))

    return tiktok

def get_random_song(protocol, hostname, port):
    '''
    Requests randon song json data from web-scraper

    ...

    Arguments
    ----------
    protocol : str
    
    hostname : str

    port : str

    ...

    Returns
    ----------
    Song
    '''

    logger.info(f'Requesting song from {hostname}: /get_random_song')
    url = f'{protocol}://{hostname}:{port}/get_random_song'
    response = requests.get(url)
    responseJson = response.json()
    logger.info(f'Response: {responseJson}')

    randomJson = responseJson.get('random')
    random = spotify(randomJson.get('region'), randomJson.get('title'), randomJson.get('artist'), randomJson.get('streams'))

    return random