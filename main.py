import os
import re
import discord
from discord.ext import commands

# List of offensive slurs (escaped for regex)
slurs = [
    r'\bfags?\b', r'\bfaggots?\b', r'\bniggers?\b', r'\bretards?\b',
    r'\bspics?\b', r'\bchinks?\b', r'\brapes?\b', r'\braped\b',
    r'\btrannys?\b', r'\btrannies?\b', r'\bhomos?\b', "slur_bot_test"
]

# Channel ID to report slur usage
REPORT_CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Initialize bot intents
intents = discord.Intents.default()
intents.message_content = True  # Correct intent for reading message content

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if any slur matches in the message content
    if any(re.search(slur, message.content.lower()) for slur in slurs):
        await message.channel.send(f"{message.author.mention}, Woah dude. Don't say that. That's warning 1.")

        report_channel = bot.get_channel(REPORT_CHANNEL_ID)
        if report_channel:
            await report_channel.send(f"Warning: {message.author.mention} used offensive language in {message.channel.mention}")

    await bot.process_commands(message)

print("Getting token from environment...")
token = os.getenv('DISCORD_BOT_TOKEN')
if token is None:
    print("Error: DISCORD_BOT_TOKEN is not set.")
else:
    print("Token found, running bot...")
    bot.run(token)
