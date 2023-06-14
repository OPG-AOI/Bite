import bot_token

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user.name}")

@bot.event
async def on_member_join(member):
    welcome_message = "Hello, Welcome to Bamboo's Fan Server! I hope you have a great time!"
    await member.send(welcome_message)

bot.run(bot_token.bot_token)