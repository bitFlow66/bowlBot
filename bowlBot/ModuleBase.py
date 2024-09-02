from discord.ext import commands


class ModuleBase(commands.Cog):

    MODULE_REGISTRY = []

    def __init_subclass__(cls, **kwargs):
        super.__init_subclass__(**kwargs)
        cls.MODULE_REGISTRY.append(cls)
        print("Subclass {} registered".format(cls.__name__))

    def getInformation(self) -> dict:
        raise NotImplementedError("Information has not been implemented.")
