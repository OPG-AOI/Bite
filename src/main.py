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

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

# initialization


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


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

#auto role fans! role

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Fans!")
    await member.add_roles(role)

#welcome message in guild

@bot.event
async def on_member_join(member):
    system_channel = member.guild.system_channel
    if system_channel is not None:
        server_title = member.guild.name
        welcome_message = f'Welcome {member.mention} to {server_title}! We hope you have a great time with us!'
        await system_channel.send(welcome_message)


# ping command


@bot.tree.command(name="ping", description="Pong!")
async def ping(interaction: discord.Interaction):
    before = datetime.now()
    await interaction.response.send_message("Pong!", ephemeral=True)

    now = datetime.now()
    formatted_ping = "{:.2f}".format(
        ((now.second * 1000.0 + now.microsecond) - (before.second * 1000.0 + before.microsecond)) / 1000.0)
    await interaction.edit_original_response(content=f"Pong! ({formatted_ping} ms)")


@bot.tree.command(name="hello", description="Hello!")
async def ping(interaction: discord.Interaction):
    before = datetime.now()
    await interaction.response.send_message("Hey 😏!", ephemeral=True)


@bot.tree.command()
async def autorole(interaction: discord.Interaction):
    if interaction.permissions.administrator:
        channel = interaction.channel

        # Your code for the autorole command
        # Prompt options to set up auto role system
        await interaction.response.send_message("Auto Role Setup:\n1. Set Auto Role\n2. Remove Auto Role")

        def check(m: discord.Message):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            message = await bot.wait_for('message', check=check, timeout=30)
        except TimeoutError:
            await channel.send("Auto Role setup timed out.")
            return

        option = message.content

        if option == "1":
            await channel.send("Mention the role to be assigned to new members:")

            try:
                role_message = await bot.wait_for('message', check=check, timeout=30)
            except TimeoutError:
                await channel.send("Role setup timed out.")
                return

            role = role_message.role_mentions[0]

            # Save the role or use it as desired
            # e.g., store in a database or assign it when new users join

            await channel.send(f"Auto Role set to {role.name}.")

        elif option == "2":
            # Remove the auto role or perform necessary actions
            await channel.send("Auto Role removed.")

        else:
            await channel.send("Invalid option.")
    else:
        await interaction.response.send_message("You must be an admin to use this command.")


# warn command
possible_warn_reasons = [
    "They were acting like a monkey and got a timeout!",
    "They were being too silly of a goose.",
    "They were acting kind of sussy and got ejected for some time.",
    "They said a nono word and went bye bye."
]


@bot.tree.command(name="warn", description="Warn a specific user with a funny message.")
@app_commands.describe(user="User to warn.")
@app_commands.default_permissions(administrator=True)
async def warn(interaction: discord.Interaction, user: discord.Member, reason: str):
    await user.timeout(timedelta(minutes=5))
    await interaction.response.send_message(f"**{user.mention}** has been warned! {possible_warn_reasons[random.randint(0, len(possible_warn_reasons) - 1)]} **Reason**: {reason}")


possible_quotes = [

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

funnypepsi_story1 = "Leonard v. Pepsico, Inc., 88 F. Supp. 2d 116, (S.D.N.Y. 1999), aff'd 210 F.3d 88 (2d Cir. 2000), more widely known as the Pepsi Points case, is an American contract law case regarding offer and acceptance. The case was brought in the United States District Court for the Southern District of New York in 1999; its judgment was written by Kimba Wood. In 1996, PepsiCo began a promotional loyalty program, in which customers could earn Pepsi Points; these points could, in turn, be traded for physical items. A television commercial for the loyalty program displayed the commercials protagonist flying a McDonnell Douglas AV-8B Harrier II vertical take off jet aircraft to school, valued at $37.4 million at the time, which could be redeemed for 7,000,000 Pepsi Points. The plaintiff, John Leonard, discovered a loophole in the promotion, allowing him to purchase Pepsi Points at 10¢ per point. Leonard promptly delivered a check for $700,008.50 to PepsiCo, attempting to purchase the jet. PepsiCo initially refuted Leonards offer, citing the humorous nature of the offer in the advertisement. Leonard then sued PepsiCo, Inc. in an effort to enforce the offer and acceptance perceived by Leonard to be made in the advertisement. In her judgment, Wood sided with PepsiCo, noting the frivolous and improbable nature of landing a fighter jet in a school zone that was portrayed by the protagonist. PepsiCo would re-release the advertisement, valuing the jet at 700,000,000 Pepsi Points. In the mid-1990s, Pepsi faced competition from Coca-Cola, and sought to attract a younger audience.[1] In March 1996, Pepsi began the Pepsi Stuff promotional campaign, allowing customers to accrue Pepsi Points that could, in turn, be redeemed for items such as T-shirts and leather jackets."


funnypepsi_story2 = "These points could be earned through purchasing Pepsi products, with labels attached to the boxes of such products. The campaign was the largest in Pepsis history.[3] To advertise the promotion, Pepsi released a series of television commercials; one of these commercials showcased a computer-generated Pepsi-branded AV-8 Harrier II, a Harrier jet manufactured by McDonnell Douglas.[2][4] The commercial, which offered the jet for 7,000,000 Pepsi Points, caught the attention of John Leonard, a 21-year-old business student. In place of a label, the promotion allowed Pepsi Points to be directly purchased for 10¢ per point, a detail noticed by Leonard, who convinced five investors to lend him a total of $700,000.[2] Leonard sent a check for $700,008.50 (including $10 for shipping and handling), and 15 labels, per promotion rules. The offer was refused by Pepsi, who referred to the promotion of the Harrier jet in the commercial as ""fanciful"" and stated its intention was to create a ""humorous and entertaining ad"".The claim alleged both breach of contract and fraud. The case was originally brought in Florida, but eventually heard in New York. The defendant, PepsiCo, moved for summary judgment pursuant to Federal Rule of Civil Procedure 56. Among other claims made, Leonard claimed that a federal judge was incapable of deciding on the matter, and that instead the decision had to be made by a jury consisting of members of the ""Pepsi Generation"" to whom the advertisement would allegedly constitute an offer."

funnypepsi_story3 = "The court presided over by Judge Kimba Wood, rejected Leonard's claims and denied recovery on several grounds, including:"

funnypepsi_story4 = "It was found that the advertisement featuring the jet did not constitute an offer under the Restatement (Second) of Contracts."
funnypepsi_story5 = "The court found that no reasonable person could have believed that the company seriously intended to convey a jet worth roughly $37.4 million for $700,000, i.e., that it was mere puffery."
funnypepsi_story6 = "The value of the alleged contract meant that it fell under the provisions of the Statute of Frauds, but the statute's requirement for a written agreement between the parties was not fulfilled, so a contract had not been formed."
funnypepsi_story7 = "In justifying its conclusion that the commercial was ""evidently done in jest"" and that ""The notion of traveling to school in a Harrier Jet is an exaggerated adolescent fantasy,"" the court made several observations regarding the nature and content of the commercial, including:"

funnypepsi_story8 = "The callow youth featured in the commercial is a highly improbable pilot, one who could barely be trusted with the keys to his parents' car, much less the prized aircraft of the United States Marine Corps."
funnypepsi_story9 = "The teenager's comment that flying a Harrier Jet to school 'sure beats the bus' evinces an improbably insouciant attitude toward the relative difficulty and danger of piloting a fighter plane in a residential area."
funnypepsi_story10 = "No school would provide landing space for a student's fighter jet, or condone the disruption the jet's use would cause."
benchmark = "---------------------------------------------------------------------------"


@bot.tree.command(name="funnypepsi", description="Tells you a funny pepsi story that happend in the 1990's")
async def funnypepsi(interaction: discord.Interaction):
    channel = bot.get_channel(interaction.channel.id)

    await interaction.response.send_message(funnypepsi_story1)
    await channel.send(benchmark)
    await channel.send(funnypepsi_story2)
    await channel.send(benchmark)
    await channel.send(funnypepsi_story3 + " " + funnypepsi_story4 + " " + funnypepsi_story5)
    await channel.send(benchmark)
    await channel.send(funnypepsi_story6 + " " + funnypepsi_story7 + " " + funnypepsi_story8)
    await channel.send(benchmark)
    await channel.send(funnypepsi_story9 + " " + funnypepsi_story10)


@bot.tree.command(name="bop", description="Bop someone on the head")
@app_commands.describe(user="User to bop.")
async def boop(interaction: discord.Interaction, user: discord.User):
    image_path = os.path.join(os.path.dirname(__file__), 'bop.png')

    with open(image_path, 'rb') as file:
        image = discord.File(file)

    message = f"{user.mention} got bopped!"
    await interaction.response.send_message(content=message, file=image)


# running the bot
bot.run(bot_token.bot_token)