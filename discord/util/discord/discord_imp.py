import logging
from discord import NotFound
from discord import Forbidden
from discord import HTTPException
from discord import PermissionOverwrite

logger = logging.getLogger(__name__)

#########################################################################################################
# Retrieves specific message provided the Discord message URL
#
# Parameters
# bot: User (Discord API)
# channel: Channel (Discord API)
# url: string
#
# Returns: None or string

async def fetchMessage(bot, channel, url):
    fetchMessage = None
    parsedMessage = url.split('/')

    # Message id will be the last param in Discord URL
    messageId = int(parsedMessage[len(parsedMessage) - 1])
    logger.info('Fetching Message')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'Message URL: {url}')
    logger.info(f'Message ID: {str(messageId)}')

    try:
        fetchedMessage = await channel.fetch_message(messageId)
        logger.info('Message Fetched')
        logger.info(f'Author: {fetchedMessage.author.display_name}')
        logger.info(f'Message: {fetchedMessage.content}')
    except NotFound as ex:
        logger.error('NotFound exception caught in fetchMessage')
        logger.error('The specified message was not found')
        logger.error(f'Channel Name: {channel.name}')
        logger.error(f'Message URL: {url}')
        logger.error(f'Message ID: {str(messageId)}')
    except Forbidden as ex:
        logger.error('Forbidden exception caught in fetchMessage')
        logger.error(f'{bot.display_name} does not have the correct permissions to retrieve the message')
        logger.error(f'Channel Name: {channel.name}')
        logger.error(f'Message URL: {url}')
        logger.error(f'Message ID: {str(messageId)}')
    except HTTPException as ex:
        logger.error('HTTPException exception caught in fetchMessage')
        logger.error('Discord fetch_message function failed to retrieve message')
        logger.error(f'Channel Name: {channel.name}')
        logger.error(f'Message URL: {url}')
        logger.error(f'Message ID: {str(messageId)}')

    return fetchedMessage

#########################################################################################################
# Retrieves the channel message history (Limited number of messages to lower sizes)
#
# Parameters
# bot: User (Discord API)
# channel: Channel (Discord API)
# msgLimit: integer
#
# Returns: None or List of Message (Discord API)

async def getMessageHistory(bot, channel, msgLimit):
    messageHistory = None
    logger.info('Retrieving Message History')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'Message History Limit: {str(msgLimit)}')
    
    try:
        messageHistory = await channel.history(limit=msgLimit).flatten()
    except Forbidden as ex:
        logger.error('Forbidden exception caught in getMessageHistory')
        logger.error(f'{bot.display_name} does not have the correct permissions to retrieve the message')
        logger.error(f'Channel Name: {channel.name}')
    except HTTPException as ex:
        logger.error('HTTPException exception caught in getMessageHistory')
        logger.error('Discord history function failed to retrieve message history')
        logger.error(f'Channel Name: {channel.name}')

    return messageHistory

#########################################################################################################
# Send message out to desired channel.  Pins message if opted for
#
# Parameters
# bot: User (Discord API)
# channel: Channel (Discord API)
# message: string
# pin: boolean

async def sendMessage(bot, channel, message, pin):
    logger.info('Sending Message')
    logger.info(f'Channel Name: {channel.name}')
    logger.info(f'Message: {message}')
    
    try:
        async_message = await channel.send(message)

        if pin:
            logger.info('Pinning Message')
            logger.info(f'Channel Name: {channel.name}')
            logger.info(f'Message: {message}')
            await async_message.pin()
    except HTTPException as ex:
        logger.error('HTTPException exception caught in sendMessage')
        logger.error('Discord send function failed to send message')
        logger.error(f'Channel Name: {channel.name}')
        logger.error(f'Message: {message}')
    except Forbidden as ex:
        logger.error('Forbidden exception caught in sendMessage')
        logger.error(f'{bot.display_name} does not have the correct permissions to retrieve the message')
        logger.error(f'Channel Name: {channel.name}')
        logger.error(f'Message: {message}')

#########################################################################################################
# Delete desired message
#
# Parameters
# message: Message (Discord API)

async def deleteMessage(message):
    logger.info('Deleting Message')
    logger.info(f'Author: {message.author.display_name}')
    logger.info(f'Message: {message.clean_content}')

    try:
        await message.delete()
    except HTTPException as ex:
        logger.error('HTTPException exception caught in deleteMessage')
        logger.error('Discord delete function failed to delete desired message')
        logger.error(f'Author: {message.author.display_name}')
        logger.error(f'Message: {message.clean_content}')

#########################################################################################################
# Creates channel in all guilds if channel doesn't exist. Channel is created with desired category name
# and desired channel name
#
# Parameters
# guilds: List of Guild (Discord API)
# categoryName: String
# channelName: String

async def createChannels(guilds, bot, categoryName, channelName, welcomeMessage):
    for guild in guilds:
        try:
            category = await createCategory(guild, categoryName)
            channel = findChannel(category, channelName)

            if channel == None:
                channel = await createChannel(guild, category, channelName)
                await sendMessage(bot, channel, welcomeMessage, True)

            await channel.set_permissions(guild.default_role, manage_messages=False, send_messages=False)
            await channel.set_permissions(bot, manage_messages=True, send_messages=True)
        except Forbidden:
            logger.error('Forbidden exception caught in createChannels')
            logger.error('Discord create text channel function failed to create desired channel')
            logger.error(f'Guild: {guild.name}')

#########################################################################################################
# Creates desired channel category if it doesn't already exist in the guild
#
# Parameters
# guild: Guild (Discord API)
# name: String
#
# Returns: Category (Discord API)

async def createCategory(guild, name):
    for category in guild.categories:
        if category.name == name:
            return category

    try:
        logger.info(f'Creating {name} channel category')
        logger.info(f'Guild: {guild.name}')
        return await guild.create_category(name)
    except Forbidden as ex:
        logger.error('Forbidden exception caught in createCategory')
        logger.error('Discord create category function failed to create desired category')
        logger.error(f'Guild: {guild.name}')
        raise ex
    except Exception as ex:
        logger.error('Unknown exception caught in createCategory')
        logger.error('Discord create category function failed to create desired category')
        logger.error(f'Guild: {guild.name}')
        raise ex

#########################################################################################################
# Creates desired channel in the desired guild and category
#
# Parameters
# guild: Guild (Discord API)
# category: Category (Discord API)
# name: String
#
# Returns: Channel (Discord API)

async def createChannel(guild, category, name):
    logger.info(f'Creating {name} channel')
    logger.info(f'Guild: {guild.name}')
    logger.info(f'Category: {category.name}')
    return await guild.create_text_channel(name, category=category)

#########################################################################################################
# Searches if desired channel name exists
#
# Parameters
# category: Category (Discord API)
# name: String
#
# Returns: None or Channel (Discord API)

def findChannel(category, name):
    for channel in category.channels:
        if channel.name == name:
            return channel

    return None