# token
import bot_token

# randomness
import random

# time stuff
from datetime import datetime
from datetime import timedelta

# discord stuff
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# initialization
@bot.event
async def on_ready():
    random.seed()
    print(f"Bot is ready. Logged in as {bot.user.name}")
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# join message :3
@bot.event
async def on_member_join(member):
    welcome_message = "Hello, Welcome to Bamboo's Fan Server! I hope you have a great time!"
    await member.send(welcome_message)

# ping command
@bot.tree.command(name="ping", description="Pong!")
async def ping(interaction: discord.Interaction):
    before = datetime.now()
    await interaction.response.send_message("Pong!", ephemeral=True)

    now = datetime.now()
    formatted_ping = "{:.2f}".format(((now.second * 1000.0 + now.microsecond) - (before.second * 1000.0 + before.microsecond)) / 1000.0)
    await interaction.edit_original_response(content=f"Pong! ({formatted_ping} ms)")

# warn command
possible_warn_reasons = [
    "They were acting like a monkey and got a timeout!",
    "They were being too silly of a goose."
]

@bot.tree.command(name="warn", description="Warn a specific user with a funny message.")
@app_commands.describe(user="User to warn.")
@app_commands.default_permissions(administrator=True)
async def warn(interaction: discord.Interaction, user: discord.Member):
    await user.timeout(timedelta(minutes=5))
    await interaction.response.send_message(f"{user.mention} has been warned! {possible_warn_reasons[random.randint(0, len(possible_warn_reasons) - 1)]}")

# running the bot
bot.run(bot_token.bot_token)