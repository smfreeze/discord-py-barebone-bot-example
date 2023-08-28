import discord

bot_token = "BOT_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'{client.user} is now online!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Hi":
        await message.channel.send(f"Ayop")
    

client.run(bot_token)
