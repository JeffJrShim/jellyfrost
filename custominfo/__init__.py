from .custominfo import CustomInfo


def setup(bot):
    cog = NoaUtils(bot)
    info_com = bot.remove_command("info")
    bot.add_cog(cog)
