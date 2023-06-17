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

@bot.tree.command(name="hello", description="Hello!")
async def ping(interaction: discord.Interaction):
    before = datetime.now()
    await interaction.response.send_message("Hey 😏!", ephemeral=True)


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

possible_quotes = ["The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The secret of getting ahead is getting started. - Mark Twain",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
    "The best revenge is massive success. - Frank Sinatra",
    "The harder I work, the luckier I get. - Gary Player",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Do not wait for the perfect moment, take the moment and make it perfect. - Unknown",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "The future depends on what you do today. - Mahatma Gandhi",
    "It always seems impossible until it's done. - Nelson Mandela",
    "The best way to predict the future is to create it. - Peter Drucker",
    "A champion is defined not by their wins but by how they can recover when they fall. - Serena Williams",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "It does not matter how many times you get knocked down, but how many times you get up. - Vince Lombardi",
    "Dream big and dare to fail. - Norman Vaughan",
    "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
    "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D",
    
     ]

@bot.tree.command(name="quote", description="Gives an inspiring quote from sombody")
async def quote(interaction: discord.Interaction):
    before = datetime.now()
    await interaction.response.send_message(possible_quotes[random.randint(0, len(possible_quotes) - 1)], ephemeral=True)

# running the bot
bot.run(bot_token.bot_token)




