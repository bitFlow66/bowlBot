from ModuleBase import ModuleBase
from discord.ext import commands


class ModuleIndex(ModuleBase):
    """
    A module to get basic information on all registered modules.

    Attributes:
        bot: Bot this module is attached to
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def index(self, ctx):
        """
        Sends a message with all registered modules and a short description

        Args:
            ctx (): Command context
        """
        modDesc = []
        for module in self.MODULE_REGISTRY:
            modDesc.append(
                f"{module.__name__} - {module.getInformation()['shortDesc']}")
        await ctx.send('\n'.join(modDesc))

    @commands.command()
    async def desc(self, ctx, moduleName: str):
        """
        Sends a message with the full description for a specified module

        Args:
            ctx (): Command context
            moduleName: Name of the module to get the description for
        """
        await ctx.send(self._getModule(moduleName).getInformation()["description"])
    @commands.command()
    async def com(self, ctx, moduleName: str):
        """
        Sends a message with all available commands for this module

        Args:
            ctx (): Command conntext
            moduleName: Name of the module to get the commands for
        """
        await ctx.send(self._getModule(moduleName).getInformation()["commands"])

    def _getModule(self, moduleName: str):
        """
        Returns a module class by name

        Args:
            moduleName: Name of the module to get

        Returns:
            Returns the module class
        """
        return [module for module in self.MODULE_REGISTRY if module.__name__ == moduleName][0]

    @staticmethod
    def getInformation() -> dict:
        """
        Some basic information for the module

        Returns:
            A dict with information on this module
        """
        return {
            "author": "flow",
            "shortDesc": "List available modules",
            "description": "This module provides a way to list all registered modules and shows a description.",
            "commands": "index  : Lists all available modules\n"
                        "desc   : Takes a module name as parameter and returns a long description\n"
                        "com    : Takes a module name and returns a list with all available commands"
        }


async def setup(bot):
    await bot.add_cog(ModuleIndex(bot))
