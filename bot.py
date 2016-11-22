import discord
import asyncio
import subprocess
import requests
import json
import os
import itertools
from lxml import html
import time
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description=description)
# Initialize bot client
# TODO: Make bot a class like normal bots.
client = discord.Client()
# Load saved data from previous instances
with open('lastchannel') as f:
    lastchannel = f.read()
print (lastchannel)
lastuser = lastchannel[22:]
lastuser = lastuser[:-7]
lastchannel = lastchannel[2:20]
lasttime = str(subprocess.Popen('cat lasttime', shell=True, stdout=subprocess.PIPE).stdout.read())
lasttime = lasttime[2:-3]
print (lastuser)
print (lastchannel)
# Bot prefix
PREFIX = '!'

@client.async_event
# Process and respond to all messages the bot receives
def on_message(message):
    """Catch a user's messages and figure out what to return."""
    foundNoCommands = True
    msg = message.content.lower()
    localtime = time.asctime( time.localtime(time.time()) )
    timezone = time.altzone
    msg = message.content
    returnMsg = ''
    messageIsClean = False
    msg = message.content.lower()
    foundNoCommands = False
    # Special returns!
    # About message
    if msg.startswith(PREFIX + 'about'):
        returnMsg = ('VictiBot is a chatbot for Team 1418\'s Discord server. Bot is currently running as ' + client.user.name + ' (ID ' + client.user.id + '). View on GitHub: https://github.com/aderhall/victibot-1')
        returnMsg = returnMsg + '\n' + ('Discuss VictiBot on VictiBot Hub: https://discord.gg/HmMMCzQ')
        messageIsClean = True
    elif


@client.async_event
# Respond on a new member joining
def on_member_join(member):
    yield from client.send_message(member.server.default_channel, '**Welcome ' + member.mention + ' to the ' + member.server.name + ' server!**')

# Respond on member leaving
@client.async_event
def on_member_remove(member):
    yield from client.send_message(member.server.default_channel, member.name + ' left the server :frowning: RIP ' + member.name)


# Get token from token.txt
with open('token.txt', 'r') as token_file:
    # Parse into a string, and get rid of trailing newlines
    token = token_file.read().replace('\n', '')
# It is only fair that whoever is running the bot should know their own token
print('Starting with token ' + token + '...')

# Start bot!
client.run(token)
