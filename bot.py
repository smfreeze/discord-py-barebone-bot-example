#Discord.py documentation is here: https://discordpy.readthedocs.io/en/stable/

import discord

bot_token = "BOT_TOKEN_HERE"

#So the bot can read messages (might need to set in your bot settings on developer portal if this doesn't work):
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


#Client Events are just events that can/will happen to your bot, you tell it what to do.

@client.event
async def on_ready(): #For when the bot first comes into the ready state
    print(f'{client.user} is now online!')


@client.event
async def on_message(message): #When a message is posted in the server it is in (you can limit which channel as shown below, you can also add some simple statements to say, add a specific prefix, like !)
    if message.author == client.user: #So the bot doesn't respond to itself
        return

    #Below is an example of if you want to limit the bot to a specific channel
    #if message.channel.name == "general":

    #Below is an example of reading message content (only when you have the correct intent) and responding to the message
    if message.content == "Hi":
        await message.channel.send(f"Ayop")
    

#Here are two other client events that can take place, a member joining and member leaving/being removed:
#@client.event
#async def on_member_join(member):
#
#@client.event
#async def on_member_remove(member):

#Starts bot
client.run(bot_token)
