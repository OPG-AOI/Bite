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

possible_quotes =[  

    "The only way to do great work is to love what you do. - Steve Jobs",
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
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "The best revenge is massive success. - Frank Sinatra",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "If you want to achieve greatness stop asking for permission. - Anonymous",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Success is not the absence of failure; it's the persistence through failure. - Aisha Tyler",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
    "The biggest risk is not taking any risk. In a world that's changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not just about making money. It's about making a difference. - Unknown",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The secret of success is to know something nobody else knows. - Aristotle Onassis",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The harder I work, the luckier I get. - Samuel Goldwyn",
    "The secret to success is to know something nobody else knows. - Aristotle Onassis",
    "Success is not the absence of failure",
    
    ]

@bot.tree.command(name="quote", description="Gives an inspiring quote from sombody")
async def quote(interaction: discord.Interaction):
    before = datetime.now()
    await interaction.response.send_message(possible_quotes[random.randint(0, len(possible_quotes) - 1)], ephemeral=True)


possible_roasts = [
    "Is your name Google? Because you have everything I'm searching for... in the wrong places.",
    "If laughter is the best medicine, your face must be curing the world.",
    "Roses are red, violets are blue, I have five fingers, and the middle one is for you.",
    "I'm not saying you're dumb, but you're so uneducated, your brain cell travels alone.",
    "I'd challenge you to a battle of wits, but I see you're unarmed.",
    "If you were any less intelligent, we'd have to water you twice a week.",
    "You bring everyone so much joy... when you leave the room.",
    "I'm jealous of people who don't know you.",
    "If I had a dollar for every brain cell you have, I'd have one dollar.",
    "You're like a light switch. Even a little kid can turn you on.",
    "I'm sorry, were you talking to me? I don't listen to insignificant people.",
    "I'd explain it to you, but I don't have any crayons.",
    "You're so full of hot air, even your imaginary friends think you're annoying.",
    "I'd call you a tool, but that would imply you're useful.",
    "Is your name Wi-Fi? Because I'm feeling a connection... failure.",
    "If you were a vegetable, you'd be a 'cute-cumber.'",
    "I'm not saying you're ugly, but you could scare the buzzards off a gut wagon.",
    "I'm surprised you haven't been banned from the gene pool yet.",
    "Your family tree must be a cactus because everyone on it is a prick.",
    "I was going to give you a nasty look, but I see you already have one.",
    "Is your face always this greasy, or are you just preparing for a slip 'n' slide?",
    "Your IQ doesn't make a u-turn. It just merges onto the highway of stupidity.",
    "If laughter is contagious, your face should be a pandemic.",
    "I'd tell you to go outside and play, but you might get lost.",
    "I'm not a doctor, but I think you need a brain transplant.",
    "Your face is just fine, but we'll have to put a bag over that personality.",
    "Is your name Homework? Because I'm not doing you, but I should be.",
    "I'm not insulting you; I'm describing you.",
    "If ignorance is bliss, you must be the happiest person on the planet.",
    "You have an entire life to be an idiot. Why not take today off?",
    "I'm sorry if my brutal honesty inconveniences your delicate sensibilities.",
    "You're not stupid. You just have bad luck when thinking.",
    "If I wanted to kill myself, I'd climb up to your ego and jump down to your IQ level.",
    "I'm not saying you're old, but your birth certificate expired.",
    "Do you ever wonder what life would be like if you'd had enough oxygen at birth?",
    "Some people just need a high-five. In the face. With a chair.",
    "It's better to let someone think you're an idiot than to open your mouth and prove it.",
    "If I had a face like yours, I'd sue my parents.",
    "I'd like to help you out. Which way did you come in?",
    "You're so dense, light bends around you.",
    "Some people should use glue sticks instead of chapstick.",
    "Did someone leave your cage open?",
    "I'm sorry, I can't hear you over the sound of how awesome I am.",
    "You're so bad at thinking, you couldn't even find your way out of a wet paper bag.",
    "I'm trying my absolute hardest to see things from your perspective, but I just can't get my head that far up my rear end.",
    "I would say you're a tool, but that would imply you're useful.",
    "Some people were dropped as a baby. You were clearly thrown at a wall.",
    "I'm sorry, were you trying to offend me? You'll have to try harder. Much, much harder.",
    "You're not a complete idiot... some parts are missing.",
    "I was going to give you a nasty look, but I see you already have one.",
    "I'm not saying you're stupid; you're just not quite as clever as you think you are.",
    "If your brain were dynamite, there wouldn't be enough to blow your hat off.",
    "I don't think you're stupid. You just have a bad luck when thinking.",
    "If you were a vegetable, you'd be a 'cute-cumber.'",
    "I'm not saying you're fat, but it looks like you were poured into your clothes and someone forgot to say 'when.'",
    "You must have been born on a highway because that's where most accidents happen.",
    "I'd call you a donkey, but that would be an insult to donkeys.",
    "Your family tree must be a cactus because everyone on it is a prick.",
    "I'm not saying you're ugly, but you make blind kids cry.",
    "I'm not saying you're boring; I'm just saying you're the reason people invent new colors.",
    "You're not pretty enough to have such an ugly personality.",
    "You're so fake that Barbie is jealous.",
    "I envy people who have never met you.",
    "You bring everyone so much joy... when you leave the room.",
    "If laughter is the best medicine, your face must be curing the world.",
    "I'm sorry, were you talking to me? I don't listen to insignificant people.",
    "I'm not a doctor, but I think you need a brain transplant.",
    "Your face is just fine, but we'll have to put a bag over that personality.",
    "I'm not insulting you; I'm describing you.",
    "You're not stupid. You just have bad luck when thinking.",
    "You're so dense, light bends around you.",
    "If I wanted to kill myself, I'd climb up to your ego and jump down to your IQ level.",
    "You're so bad at thinking, you couldn't even find your way out of a wet paper bag.",
    "I'm trying my absolute hardest to see things from your perspective, but I just can't get my head that far up my rear end.",
    "I would say you're a tool, but that would imply you're useful.",
    "Some people were dropped as a baby. You were clearly thrown at a wall.",
    "I'm sorry, were you trying to offend me? You'll have to try harder. Much, much harder.",
    "You're not a complete idiot... some parts are missing.",
    "I'm not saying you're stupid; you're just not quite as clever as you think you are.",
    "I'm not saying you're ugly, but you make blind kids cry.",
    "I'm not saying you're boring; I'm just saying you're the reason people invent new colors.",
    "You're not pretty enough to have such an ugly personality.",
    "I envy people who have never met you."
]


@bot.tree.command(name="roast", description="Roasts a person in the")
@app_commands.describe(user="User to roast.")
@app_commands.default_permissions(administrator=False)
async def warn(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f"{user.mention} heres something for you: {possible_roasts[random.randint(0, len(possible_roasts) - 1)]}")

# running the bot
bot.run(bot_token.bot_token)




