from io import BytesIO
from ModuleBase import ModuleBase
from modules.mazer.Maze import Maze

from discord.ext import commands
import discord


class Mazer(ModuleBase):

    """
    A module which utilises the loop-erasing random walk to create non-biased mazes
    and presents it as a png.

    Attributes:
        bot: Bot this module will be attached to.
    """

    def __init__(self, bot):
        self.bot = bot
        # TODO: Make a maze turtle which takes a maze as parameter and is able to walk in the maze -> Turtle(Maze())

    @commands.command()
    async def maze(self, ctx: commands.Context, collumns: int = 20, rows: int = 20):
        # TODO: Limit collumns and rows for performance/time
        async with ctx.typing():
            # TODO: Create maze in a separate (discord) thread
            maze = Maze(collumns=collumns, rows=rows)
            with BytesIO() as image_binary:
                maze.getImage().save(image_binary, "PNG")
                image_binary.seek(0)
                await ctx.send(
                    file=discord.File(
                        fp=image_binary, filename=f"maze-{ctx.author}.png"
                    )
                )

    @staticmethod
    def getInformation() -> dict:
        return {
            "author": "flow",
            "shortDesc": "Creates a maze to solve as png.",
            "description": "Creates a maze as a png that can be solved.",
            "commands": "maze   :   Creates a Maze and returns a png of it (Syntax: maze collumns: int rows: int)",
        }


async def setup(bot):
    await bot.add_cog(Mazer(bot))
