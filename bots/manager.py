import discord
from discord.ext import commands
import logging
import asyncio
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
admin_ids = [int(x.strip()) for x in os.getenv("OWNER_IDS", "").split(",") if x.strip()] #makes a list of admin IDs

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

prefix = os.getenv("PREFIX")

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")

@bot.command()
@commands.has_permissions(administrator=True)
async def exodus(ctx):
    guild = ctx.guild
    # Delete all channels
    for channel in list(guild.channels):
        try:
            await channel.delete()
        except Exception as e:
            print(f"Failed to delete channel {channel}: {e}")
    # Create one channel called "Abd"
    abd_channel = await guild.create_text_channel("Abd")
    await abd_channel.send("Exodus complete. Only this channel remains.")

@bot.command()
async def spamdm(ctx, num: int, user: discord.User, *, content: str):
    for _ in range(num):
        try:
            await user.send(content)
        except Exception as e:
            await ctx.send(f"Failed to send DM: {e}")
    await ctx.send(f"Sent {num} messages to {user.mention}.")


@bot.command()
async def help(ctx):
    # Count running bot files (including the manager script itself)
    bots_folder = os.path.dirname(__file__)  # current folder
    bot_files = [f for f in os.listdir(bots_folder) if f.endswith(".py") and f != os.path.basename(__file__)]
    bot_count = len(bot_files)

    embed = discord.Embed(
        title="Manager Bot Help",
        description=f"Here's a list of available commands and how to use them:\n**Currently running bots:** {bot_count}",
        color=discord.Color.blurple(),
    )

    # Manager bot commands
    embed.add_field(
        name=f"{prefix}exodus",
        value="Deletes all channels in the server and creates a single channel called 'Abd'. **Administrator only.**",
        inline=False,
    )
    embed.add_field(
        name=f"{prefix}spamdm <num> <user> <content>",
        value="Sends `<num>` DMs to the specified `<user>` with the `<content>` message.\nExample: `!spamdm 5 @User Hello!`",
        inline=False,
    )

    # Slave bot commands (DM bot)
    embed.add_field(
        name="Slave Bot Commands",
        value=(
            f"`!dm <user> <message>` – Send a DM to a user with optional key=value overrides.\n"
            f"Optional parameters:\n"
            f"- `delay` (seconds between messages, default 0.5)\n"
            f"- `count` (number of messages, default 1)\n"
            f"- `number` (minimum bot ID required, default 1)\n"
            f"Example: `!dm @User Hello! count=3 delay=1 number=2`"
        ),
        inline=False,
    )

    embed.add_field(
        name=f"{prefix}help",
        value="Shows this help message in a neat embed.",
        inline=False,
    )

    embed.set_footer(text="Manager Bot • Made by @12_ad")
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)

    await ctx.send(embed=embed)


@bot.command()
async def shutdown(ctx):
    """Shuts down the manager bot (owner only)."""
    if ctx.author.id not in admin_ids:
        await ctx.send("❌ You are not authorized to shut down the bot.")
        return

    await ctx.send("⚠️ Shutting down all bots...")

    # Call the batch file to stop all bots
    bat_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "stop_bots.bat")
    if os.path.exists(bat_path):
        subprocess.Popen([bat_path], shell=True)
        await ctx.send("✅ Stop command sent. Exiting manager bot...")
    else:
        await ctx.send("❌ stop_bots.bat not found, shutting down manager only.")

    # Shut down the manager bot
    await bot.close()


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
