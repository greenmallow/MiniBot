import discord

from secrets import BOT_TOKEN


BOT_NAME = 'MiniBot' # Bot's name in sent messages
PREFIX = '$$' # The prefix bot commands will start with
COMMANDS = ('config', 'help', 'ping')

# default settings, which can be adjusted via $$config
settings = {'dad_on': True}

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
            command = tokens[0].lower()
            arguments = tokens[1:]

            if command == 'help':
                # Send a list of all available commands
                preamble = f"The following commands are available. (All commands are prefixed with '{PREFIX}')"
                response = f"{preamble}\n`{str(COMMANDS)[1:-1]}`"
                    
                await message.channel.send(response)

            elif command == 'config':
                # Adjust the bot's settings

                # This command expects arguments, so it sends a usage
                # message if none are provided
                if len(arguments) > 0:
                    await message.channel.send(adjust_settings(arguments))
                else:
                    await message.channel.send(f'Usage: `{PREFIX}config [setting] ["on"/"off"]`')

            elif command == 'ping':
                # Reply to ping with "Pong!"
                await message.channel.send('Pong!')

            else:
                await message.channel.send(f"Sorry, I don't recognise the command `{command}`.")

    elif message.content.lower().startswith("i'm ") and settings['dad_on']:
        # Implements the "Hi hungry, I'm Dad" style joke
        iam = message.content[len("I'm "):]
        await message.channel.send(f"Hi {iam}, I'm {BOT_NAME}!")


def adjust_settings(arguments):
    """
    Adjust the bot's settings based on parameters passed to $$config.
    Returns a string to be sent to the user.
    """
    setting = arguments[0].lower()
    parameters = arguments[1:]

    if setting == 'dad_on':
        # Expects a parameter "on" or "off"
        if len(parameters) >= 1:
            if parameters[0].lower() == "on":
                settings['dad_on'] = True
            elif parameters[0].lower() == "off":
                settings['dad_on'] = False
            else:
                return f'Usage: `{PREFIX}config dad_on ["on"/"off"]`'
            
            # Setting was successfully set
            return f"Setting 'dad_on' was set to `{settings['dad_on']}`"

        else:
            # No parameters provided.
            return f'Usage: `{PREFIX}config dad_on ["on"/"off"]`'
    else:
        return f"Sorry, I don't recognise the setting `{setting}`."


# Run the bot using the token from secrets.py
client.run(BOT_TOKEN)