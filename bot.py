import discord

from secrets import BOT_TOKEN


BOT_NAME = 'MiniBot' # Bot's name in sent messages
PREFIX = '$$' # The prefix bot commands will start with
COMMANDS = ('help',)

client = discord.Client()


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
        tokens = msg.split()

        if len(tokens) > 0:
            command = tokens[0]
            arguments = tokens[1:]

            if command == 'help':
                # Sends a list of all available commands
                preamble = f"The following commands are available. (All commands are prefixed with '{PREFIX}')"
                response = f"{preamble}\n`{str(COMMANDS)[1:-1]}`"
                    
                await message.channel.send(response)
            else:
                await message.channel.send(f"Sorry, I don't recognise the command `{command}`.")

    elif message.content.lower().startswith("i'm "):
        # Implements the "Hi hungry, I'm Dad" style joke
        iam = message.content[len("I'm "):]
        await message.channel.send(f"Hi {iam}, I'm {BOT_NAME}!")


# Run the bot using the token from secrets.py
client.run(BOT_TOKEN)