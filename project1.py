import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Its ready!')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content in ['Hi', 'Hello', 'hi', 'hello']:
        await message.channel.send('Welcome to the Shit bot')

client.run('Discord-Bot-Token')
