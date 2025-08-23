import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# Use filename as numeric ID
id = int(os.path.splitext(os.path.basename(__file__))[0])

load_dotenv()
token = os.getenv(f"BOT{id}")
if token is None:
    raise ValueError(f"No token found for BOT{id} in .env")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
prefix = os.getenv("PREFIX")
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

@bot.command()
async def dm(ctx, user: discord.User, *, message_and_kwargs: str):
    # Default values
    delay = 0.5
    count = 1
    number = 1

    # Split message and optional key=value kwargs
    parts = message_and_kwargs.split()
    message_parts = []
    for part in parts:
        if "=" in part:
            key, value = part.split("=", 1)
            key = key.lower()
            if key == "delay":
                delay = float(value)
            elif key == "count":
                count = int(value)
            elif key == "number":
                number = int(value)
        else:
            message_parts.append(part)

    message = " ".join(message_parts)

    if id > number:
        return

    for _ in range(count):
        await user.send(message)
        await asyncio.sleep(delay)

    await ctx.send(f"{count} DM(s) sent to {user.mention}")


bot.run(token)
