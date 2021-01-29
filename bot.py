import random

import discord
from discord.ext import commands

from bot_secrets import BOT_TOKEN

BOT_NAME = 'MiniBot' # Bot's name in sent messages
PREFIX = '$$' # The prefix bot commands will start with
COMMANDS = ('8ball', 'commands', 'config', 'ping', 'settings')

# Default settings, which can be adjusted via $$config
bot_settings = {'dad_on': True}

client = commands.Bot(command_prefix = PREFIX)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('Press CTRL-C to stop.')


# Currently disabled due to the commands not being called if this
# function is implemented

# @client.event
# async def on_message(message):
#     # Ignore the message if it was sent by the bot
#     if message.author == client.user:
#         return

#     if message.content.lower().startswith("i'm ") and bot_settings['dad_on']:
#         # Implements the "Hi hungry, I'm Dad" style joke
#         iam = message.content[len("I'm "):]
#         await message.channel.send(f"Hi {iam}, I'm {BOT_NAME}!")


@client.command(brief = 'Shows a list of all available commands')
async def commands(ctx):
    # Send a list of all available commands
    preamble = f"The following commands are available. (All commands are prefixed with '{PREFIX}')"
    response = f"{preamble}\n`{str(COMMANDS)[1:-1]}`"
        
    await ctx.send(response)


@client.command(brief = 'Used to adjust settings')
async def config(ctx, *args):
    """
    Adjust the bot's settings. This command expects arguments, so it
    sends a usage message if none are provided
    """

    if len(args) > 0:
        await ctx.send(adjust_settings(args))
    else:
        await ctx.send(f'Usage: `{PREFIX}config [setting] ["on"/"off"]`')


@client.command(name = '8ball', brief = 'Gives an answer to yes-or-no questions')
async def eight_ball(ctx):
    # Gives a random answer to yes-or-no questions
    ball_answers = ['Yes', 'Certainly', 'Definitely', 'It appears so',
                    'Maybe', 'Possibly', 'I am unsure',
                    'No', 'Certainly not', 'Nope', 'Definitely not']

    await ctx.send(random.choice(ball_answers) + '.')


@client.command(brief = 'Replies to ping with "Pong!"')
async def ping(ctx):
    # Reply to ping with 'Pong!'
    await ctx.send('Pong!')


@client.command(brief = "Shows the state of the bot's settings")
async def settings(ctx):
    # View all of the current settings
    await ctx.send(f'`{bot_settings}`')


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
                bot_settings['dad_on'] = True
            elif parameters[0].lower() == "off":
                bot_settings['dad_on'] = False
            else:
                return f'Usage: `{PREFIX}config dad_on ["on"/"off"]`'
            
            # Setting was successfully set
            return f"Setting 'dad_on' was set to `{bot_settings['dad_on']}`"

        else:
            # No parameters provided.
            return f'Usage: `{PREFIX}config dad_on ["on"/"off"]`'
    else:
        return f"Sorry, I don't recognise the setting `{setting}`."


# Run the bot using the token from bot_secrets.py
client.run(BOT_TOKEN)