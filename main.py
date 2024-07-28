import os
import discord
from discord.ext import commands

slurs = ['fag', 'faggot', 'nigger', 'retard', 'spic', 'chink', 'rape', 'raped', 'tranny', 'trany', 'homo']

REPORT_CHANNEL_ID = 1266626575261106186

intents = discord.Intents.default()
intents.message_content = True  # Correct intent for reading message content

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Goliath. On. Line.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(slur in message.content.lower() for slur in slurs):
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