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
from dislash.application_commands._modifications.old import (
    send_with_components,
)

class CustomInfo(commands.Cog):
    """
    A cog for information on Toli.
    """
    
    __author__ = ["JeffJrShim"]
    __version__ = "1.0.0"
    
    def __init__(self, bot):
        self.bot = bot
        if not hasattr(commands.Context, "sendi"):
            commands.Context.sendi = send_with_components

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
        owner = self.bot.get_user(726802094371242074)
        embed_links = await ctx.embed_requested()
        author_repo = "https://github.com/Twentysix26"
        org_repo = "https://github.com/Cog-Creators"
        red_repo = org_repo + "/Red-DiscordBot"
        red_pypi = "https://pypi.org/project/Red-DiscordBot"
        support_server_url = "https://discord.gg/wgSA5VkYCa"
        dpy_repo = "https://github.com/Rapptz/discord.py"
        python_url = "https://www.python.org/"
        since = datetime.datetime(2016, 1, 2, 0, 0)
        days_since = (datetime.datetime.utcnow() - since).days
        python_version = "[`{}.{}.{}`]({})".format(*sys.version_info[:3], python_url)
        dpy_version = "[`{}`]({})".format(discord.__version__, dpy_repo)
        red_version = "[`{}`]({})".format(version_info, red_pypi)
        embed = discord.Embed(description=f"**:wave: Hi, I am {ctx.me.name}!**\nI am currently running on version **__{red_version}__**\n**Support Server**\nJoin me on my support server: [Toli Support]({support_server_url})\n**Invite me to your Server**\nHere is a link to invite me to your guild as well: [Toli invite link](https://discord.com/api/oauth2/authorize?client_id=943931974568001546&permissions=0&scope=bot)\n**I am listed in follow bot lists:**\n:white_check_mark: [DBL (top.gg)](https://top.gg/bot/943931974568001546)\n✅ [Discord Bots](https://discord.bots.gg/bots/943931974568001546)\n✅ [discordbotlist.com](https://discordbotlist.com/bots/toli)\n✅ [Bots on Discord](https://bots.ondiscord.xyz/bots/943931974568001546)\n✅ [Bots for Discord](https://botsfordiscord.com/bot/943931974568001546)\nI am on **{len(bot.guilds)}** guilds!" ,color=await ctx.embed_color())
        embed.set_thumbnail(url=ctx.me.avatar_url)
        await ctx.send(embed=embed, reference=ctx.message.to_reference())