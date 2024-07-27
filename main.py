import os
import discord
from discord.ext import commands

slurs = ['fag', 'faggot', 'nigger', 'retard', 'spic', 'chink']

REPORT_CHANNEL_ID = 1266626575261106186

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Goliath. On. Line.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(slur in message.content.lower() for slur in slurs):
        await message.channel.send(f"{message.author.mention}, Woah dude. Dont Say that. Thats warning 1.")

        report_channel = bot.get_channel(REPORT_CHANNEL_ID)
        if report_channel:
            await report_channel.send(f"Warning: {message.author.mention}  used offensive language in {message.channel.mention}")

    await bot.process_commands(message)
    token = os.getenv('DISCORD_BOT_TOKEN')
    bot.run(token)