from ModuleBase import ModuleBase
from discord.ext import commands

class Echo(ModuleBase):
    """
    A module implementing the `echo` command for testing purposes.

    Attributes:
        bot: Bot this module is attached to.
    """

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def echo(self, ctx, text: str):
        """
        Sends a message with the content of its argument.

        Args:
            ctx (): Command context,
            text: the string to be echoed back.
        """
        await ctx.send(text)


    @staticmethod
    def getInformation() -> dict:
        """
        Some basic information for the module.

        Returns:
            A dict with information on this module.
        """

        return {
            "author": "md",
            "shortDesc": "The `echo` command.",
            "description": "A test module that implements the `echo` command.",
            "commands": "echo  : sends back the argument string unchanged."
        }


async def setup(bot):
    await bot.add_cog(Echo(bot))
