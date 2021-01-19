import discord

from secrets import BOT_TOKEN

client = discord.Client()

BOT_NAME = 'Minimally Entertaining Bot' # Bot's name in sent messages
PREFIX = '$$' # The prefix bot commands will start with


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    # Ignore the message if it was sent by the bot
    if message.author == client.user:
        return

    # Commands beginning with the chosen prefix
    if message.content.startswith(PREFIX):
        # msg represents the message with the prefix removed
        msg = message.content[len(PREFIX):]

    elif message.content.lower().startswith("i'm "):
        # Implements the 'Hi hungry, I'm Dad'-type joke
        iam = message.content[len("I'm "):]
        await message.channel.send(f"Hi {iam}, I'm {BOT_NAME}!")


# Run the bot using the token from secrets.py
client.run(BOT_TOKEN)