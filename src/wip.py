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

@bot.tree.command(name="report", description="Report a problem to a administrator")
async def report(ctx, report_text, interaction: discord.Interaction):
    # Find a member with administrator permissions in the server
    admin = discord.utils.get(ctx.guild.members, guild__id=ctx.guild.id, permissions=discord.Permissions(administrator=True))

    if admin:
        # Send the report message to the administrator via private message
        report_message = f'Report from {ctx.author.display_name} ({ctx.author.name}):\n{report_text}'
        await admin.send(report_message)
        await ctx.send('Report submitted to the administrator. Thank you!')
    else:
        await ctx.send('No administrator found in this server.')