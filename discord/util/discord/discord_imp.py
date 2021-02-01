import logging
from discord import channel
from discord import Message
from discord import NotFound
from discord import Forbidden
from discord import HTTPException
from discord import PermissionOverwrite

logger = logging.getLogger(__name__)

#########################################################################################################

async def fetchMessage(bot, channel, url) -> str:
    '''
    Retrieves specific message provided the Discord message URL

    ...

    Arguments
    ----------
    bot : discord.User
    
    channel : discord.Channel
    
    url : str
    '''

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

async def getMessageHistory(bot, channel, msgLimit) -> [Message]:
    '''
    Retrieves the channel message history (Limited number of messages to lower sizes)

    ...

    Arguments
    ----------
    bot : discord.User
    
    channel : discord.Channel
    
    msgLimit : int
    '''

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

async def sendMessage(bot, channel, message, pin) -> None:
    '''
    Send message out to desired channel.  Pins message if opted for
    
    ...

    Arguments
    ----------
    bot : discord.User
    
    channel : discord.Channel
    
    message : str
    
    pin : boolean
    '''

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

async def deleteMessage(message) -> None:
    '''
    Delete desired message

    ...

    Arguments
    ----------
    message : discord.Message
    '''

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

async def createChannels(guilds, bot, categoryName, channelName, welcomeMessage) -> None:
    '''
    Creates channel in all guilds if channel doesn't exist. Channel is created with desired category name
    and desired channel name

    ...

    Arguments
    ----------
    guilds : [discord.Guild]

    bot : discord.User
    
    categoryName : str
    
    channelName : str

    welcomeMessage : str
    '''
    
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

async def createCategory(guild, name) -> None:
    '''
    Creates channel in all guilds if channel doesn't exist. Channel is created with desired category name
    and desired channel name

    ...

    Arguments
    ----------
    guild : discord.Guild
    
    name : str
    '''

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

async def createChannel(guild, category, name) -> channel:
    '''
    Creates desired channel in the desired guild and category

    ...

    Arguments
    ----------
    guild : discord.Guild
    
    category : discord.Category
    
    name : str
    '''

    logger.info(f'Creating {name} channel')
    logger.info(f'Guild: {guild.name}')
    logger.info(f'Category: {category.name}')
    return await guild.create_text_channel(name, category=category)

#########################################################################################################

def findChannel(category, name) -> channel:
    '''
    Searches if desired channel name exists

    ...

    Arguments
    ----------
    category : discord.Category
    
    name : str
    '''

    for channel in category.channels:
        if channel.name == name:
            return channel

    return None