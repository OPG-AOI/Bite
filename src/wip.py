# token
import bot_token

# import os
import os

# randomness
import random

# time stuff
from datetime import datetime
from datetime import timedelta

# discord stuff
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

