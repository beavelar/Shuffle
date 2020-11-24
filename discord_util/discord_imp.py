from discord import NotFound
from discord import Forbidden
from discord import HTTPException
from discord import PermissionOverwrite

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

    print('-----------------------------------------------------------------------------')
    print('Fetching Message')
    print(f'Channel Name: {channel.name}')
    print(f'\nMessage URL: {url}')
    print(f'\nMessage ID: {str(messageId)}')
    print('-----------------------------------------------------------------------------\n')

    try:
        fetchedMessage = await channel.fetch_message(messageId)
        
        print('-----------------------------------------------------------------------------')
        print('Message Fetched')
        print(f'Author: {fetchedMessage.author.display_name}')
        print(f'\nMessage:\n{fetchedMessage.content}')
        print('-----------------------------------------------------------------------------\n')
    except NotFound as ex:
        print('-----------------------------------------------------------------------------')
        print('NotFound exception caught in fetchMessage')
        print('The specified message was not found')
        print(f'Channel Name: {channel.name}')
        print(f'\nMessage URL: {url}')
        print(f'\nMessage ID: {str(messageId)}')
        print('-----------------------------------------------------------------------------\n')
    except Forbidden as ex:
        print('-----------------------------------------------------------------------------')
        print('Forbidden exception caught in fetchMessage')
        print(f'{bot.display_name} does not have the correct permissions to retrieve the message')
        print(f'Channel Name: {channel.name}')
        print(f'\nMessage URL: {url}')
        print(f'\nMessage ID: {str(messageId)}')
        print('-----------------------------------------------------------------------------\n')
    except HTTPException as ex:
        print('-----------------------------------------------------------------------------')
        print('HTTPException exception caught in fetchMessage')
        print('Discord fetch_message function failed to retrieve message')
        print(f'Channel Name: {channel.name}')
        print(f'\nMessage URL: {url}')
        print(f'\nMessage ID: {str(messageId)}')
        print('-----------------------------------------------------------------------------\n')

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

    print('-----------------------------------------------------------------------------')
    print('Retrieving Message History')
    print(f'Channel Name: {channel.name}')
    print(f'\nMessage History Limit: {str(msgLimit)}')
    print('-----------------------------------------------------------------------------\n')
    
    try:
        messageHistory = await channel.history(limit=msgLimit).flatten()
    except Forbidden as ex:
        print('-----------------------------------------------------------------------------')
        print('Forbidden exception caught in getMessageHistory')
        print(f'{bot.display_name} does not have the correct permissions to retrieve the message')
        print(f'Channel Name: {channel.name}')
        print('-----------------------------------------------------------------------------\n')
    except HTTPException as ex:
        print('-----------------------------------------------------------------------------')
        print('HTTPException exception caught in getMessageHistory')
        print('Discord history function failed to retrieve message history')
        print(f'Channel Name: {channel.name}')
        print('-----------------------------------------------------------------------------\n')

    return messageHistory

#########################################################################################################
# Send message out to desired channel
#
# Parameters
# bot: User (Discord API)
# channel: Channel (Discord API)
# message: string

async def sendMessage(bot, channel, message):
    print('-----------------------------------------------------------------------------')
    print('Sending Message')
    print(f'Channel Name: {channel.name}')
    print(f'\nMessage:\n{message}')
    print('-----------------------------------------------------------------------------\n')
    
    try:
        await channel.send(message)
    except HTTPException as ex:
        print('-----------------------------------------------------------------------------')
        print('HTTPException exception caught in sendMessage')
        print('Discord send function failed to send message')
        print(f'Channel Name: {channel.name}')
        print(f'\nMessage:\n{message}')
        print('-----------------------------------------------------------------------------\n')
    except Forbidden as ex:
        print('-----------------------------------------------------------------------------')
        print('Forbidden exception caught in sendMessage')
        print(f'{bot.display_name} does not have the correct permissions to retrieve the message')
        print(f'Channel Name: {channel.name}')
        print(f'\nMessage:\n{message}')
        print('-----------------------------------------------------------------------------\n')

#########################################################################################################
# Delete desired message
#
# Parameters
# message: Message (Discord API)

async def deleteMessage(message):
    print('-----------------------------------------------------------------------------')
    print('Deleting Message')
    print(f'Author: {message.author.display_name}')
    print(f'\nMessage:\n{message.clean_content}')
    print('-----------------------------------------------------------------------------\n')

    try:
        await message.delete()
    except HTTPException as ex:
        print('-----------------------------------------------------------------------------')
        print('HTTPException exception caught in deleteMessage')
        print('Discord delete function failed to delete desired message')
        print(f'Author: {message.author.display_name}')
        print(f'\nMessage:\n{message.clean_content}')
        print('-----------------------------------------------------------------------------\n')

#########################################################################################################
# Creates channel in all guilds if channel doesn't exist. Channel is created with desired category name
# and desired channel name
#
# Parameters
# guilds: List of Guild (Discord API)
# categoryName: String
# channelName: String
#
# Returns: List of Channel (Discord API)

async def createChannels(guilds, bot, categoryName, channelName):
    channels = []

    for guild in guilds:
        try:
            category = await createCategory(guild, categoryName)
            channel = findChannel(category, channelName)

            if channel == None:
                print('-----------------------------------------------------------------------------')
                print(f'Creating {channelName} channel')
                print(f'Guild: {guild.name}')
                print(f'Category: {category.name}')
                print('-----------------------------------------------------------------------------\n')

                channel = await guild.create_text_channel(channelName, category=category)

                print('-----------------------------------------------------------------------------')
                print(f'Successfully created {channelName} channel')
                print(f'Guild: {guild.name}')
                print(f'Category: {category.name}')
                print('-----------------------------------------------------------------------------\n')

            await channel.set_permissions(guild.default_role, manage_messages=False, send_messages=False)
            await channel.set_permissions(bot, manage_messages=True, send_messages=True)
        except Forbidden:
            print('-----------------------------------------------------------------------------')
            print('Forbidden exception caught in createChannel')
            print('Discord create text channel function failed to create desired channel')
            print(f'Guild: {guild.name}')
            print('-----------------------------------------------------------------------------\n')
        
        channels.append(channel)

    return channels


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
        print('-----------------------------------------------------------------------------')
        print(f'Creating {name} channel category')
        print(f'Guild: {guild.name}')
        print('-----------------------------------------------------------------------------\n')

        return await guild.create_category(name)

        print('-----------------------------------------------------------------------------')
        print(f'Successfully created {name} channel category')
        print(f'Guild: {guild.name}')
        print('-----------------------------------------------------------------------------\n')
    except Forbidden as ex:
        print('-----------------------------------------------------------------------------')
        print('Forbidden exception caught in createCategory')
        print('Discord create category function failed to create desired category')
        print(f'Guild: {guild.name}')
        print('-----------------------------------------------------------------------------\n')

        raise ex
    except Exception as ex:
        print('-----------------------------------------------------------------------------')
        print('Unknown exception caught in createCategory')
        print('Discord create category function failed to create desired category')
        print(f'Guild: {guild.name}')
        print('-----------------------------------------------------------------------------\n')

        raise ex

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