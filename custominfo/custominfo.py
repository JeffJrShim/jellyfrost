import random
from typing import Union
import discord
import humanize
from discord.ext import commands
from redbot.core.utils import chat_formatting as chat
from redbot.core import commands
from redbot.core.utils.chat_formatting import box, humanize_list
from redbot import version_info
import datetime
import sys

class CustomInfo(commands.Cog):
    """
    A cog for information on Toli.
    """
    
    __author__ = ["JeffJrShim"]
    __version__ = "1.0.0"
    
    def __init__(self, bot):
        self.bot = bot

    def cog_unload(self):
        global info_com
        global invite_com
        if info_com:
            try:
                self.bot.remove_command("info")
            except Exception as e:
                log.info(e)
        self.bot.add_command(info_com)
        
    @commands.command()
    async def info(self, ctx):
        owner = self.bot.get_user(550984303526281219)
        embed_links = await ctx.embed_requested()
        author_repo = "https://github.com/Twentysix26"
        org_repo = "https://github.com/Cog-Creators"
        red_repo = org_repo + "/Red-DiscordBot"
        red_pypi = "https://pypi.org/project/Red-DiscordBot"
        support_server_url = "https://discord.gg/RSAetqdhRU"
        dpy_repo = "https://github.com/Rapptz/discord.py"
        python_url = "https://www.python.org/"
        since = datetime.datetime(2016, 1, 2, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days
        python_version = "[`{}.{}.{}`]({})".format(*sys.version_info[:3], python_url)
        dpy_version = "[`{}`]({})".format(discord.__version__, dpy_repo)
        red_version = "[`{}`]({})".format(version_info, red_pypi)
        jef = self.bot.get_user(726802094371242074)
        embed = discord.Embed(color=await ctx.embed_color())
        embed.add_field(name=f"{ctx.me.name}'s Owner", value=owner)
        embed.add_field(
            name="Versions",
            value=f"<:Python:928926404077289533> {python_version}\n<:dpy:926811146101596222> {dpy_version}\n<:red:926316873400872990> {red_version}",
        )
        embed.add_field(
            name=f"About {ctx.me.name}",
            value=f"{ctx.me.name} is an instance of [Red, an open source Discord bot]({red_repo}) created by [Twentysix]({author_repo}) and improved by many with many 3rd party cogs, written by many other Cog Creators, and {jef.name} himself. Please do not bother Red's support server with inquiries regarding this bot, please use the [support server]({support_server_url}), instead. \n\nRed is backed by a passionate community who contributes and creates content for everyone to enjoy. Join us today and help us improve!\n\n(c) Cog Creators, and {jef.name}",
            inline=False,
        )
        embed.set_thumbnail(url=ctx.me.avatar_url)
        await ctx.send(embed=embed, reference=ctx.message.to_reference())
