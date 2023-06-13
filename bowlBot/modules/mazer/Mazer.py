from ModuleBase import ModuleBase
from modules.mazer.Maze import Maze


class Mazer(ModuleBase):

    """
    A module which utilises the loop-erasing random walk to create non-biased mazes
    and presents it as a png.

    Attributes:
        bot: Bot this module will be attached to.
    """

    def __init__(self, bot):
        self.bot = bot
        maze = Maze()
        # TODO: Make a maze turtle which takes a maze as parameter and is able to walk in the maze -> Turtle(Maze())

    @staticmethod
    def getInformation() -> dict:
        return {
            "author": "flow",
            "shortDesc": "Creates a maze to solve as png.",
            "description": "Creates a maze as a png that can be solved.",
            "commands": "",
        }


async def setup(bot):
    await bot.add_cog(Mazer(bot))
