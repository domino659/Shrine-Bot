import discord
from discord.ext import commands

from os import listdir, getenv
from os.path import isfile, join

import sys, traceback

from unidecode import unidecode

from utils import env

intents = discord.Intents.default()
intents.members = True

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['>']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)

# This is the directory all are located in.
cogs_dir = "cogs"

bot = commands.Bot(command_prefix=get_prefix, intents = intents, description='ShrineBot')

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.display_name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    
    # Bot Playing Status
    await bot.change_presence(activity=discord.Streaming(name='Otter Rescue', url='https://www.twitch.tv/marinemammalrescue'))
    print(f'Successfully logged in and booted...!')


# @bot.event
# async def on_member_join(member):
#     general_channel: discord.TextChannel = bot.get_channel(getenv("PRIMARY_CHANNEL"))
#     await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")


@bot.event
async def on_message(message):
    if not message.content.startswith('>'):
        string = unidecode(message.content).lower()
        print(string)
        if "fleur" in string:
            await message.channel.send("Grossier Merle")

            print(message.content)
    await bot.process_commands(message)


bot.run(getenv("TOKEN"), bot=True, reconnect=True)