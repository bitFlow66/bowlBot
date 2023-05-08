from ModuleBase import ModuleBase
from discord.ext import commands

class Echo(ModuleBase):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def echo(self, ctx):
        reply_text = ctx.message.content.removeprefix("!echo").strip()
        print("echo:", reply_text)
        await ctx.send(reply_text)


async def setup(bot):
    await bot.add_cog(Echo(bot))
