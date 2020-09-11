import random as rand

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
    await sendMessage(user, channel, helpMenu)

#########################################################################################################
# Displays the current top regional song (Global/US) onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)

async def top(user, channel):
    topGlobalSong = getTopSong('regional', 'global')
    topUSSong = getTopSong('regional', 'us')
    report = topGlobalSong.generateTopSongReport() + '\n\n' + topUSSong.generateTopSongReport()
    
    await sendMessage(user, channel, report)

#########################################################################################################
# Displays the current top TikTok song onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)

async def tiktok(user, channel):
    topTikTokSong = getTopTikTokSong()
    report = topTikTokSong.generateTopSongReport()
    
    await sendMessage(user, channel, report)

#########################################################################################################
# Displays a random song (compiled from top songs) onto the desired Discord channel
#
# Parameters
# user: User (Discord API)
# channel: Channel (Discord API)

async def random(user, channel):
    songs = getTop200List('regional','us')
    songs.extend(getTop200List('regional', 'global'))
    songs.extend(getTop200List('viral', 'global'))
    songs.extend(getTop200List('viral', 'global'))

    randomIndex = rand.randint(0, len(songs))

    await sendMessage(user, channel, songs[randomIndex].generateRandomSongReport())

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