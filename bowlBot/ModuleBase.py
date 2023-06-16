import logging

from discord.ext import commands


class ModuleBase(commands.Cog):
    MODULE_REGISTRY = []

    def __init_subclass__(cls, **kwargs):
        super.__init_subclass__(**kwargs)
        cls.MODULE_REGISTRY.append(cls)
        # Create a logger and add handler + formatter
        cls.logger: logging.Logger = logging.getLogger(cls.__name__)
        ch = logging.StreamHandler()
        # TODO: Configure formatter
        formatter = logging.Formatter(
            "[%(levelname)s - %(asctime)s]: [Module -> %(name)s, File -> %(module)s, Function -> %(funcName)s] %(message)s"
        )
        ch.setFormatter(formatter)
        cls.logger.addHandler(ch)

    def getInformation(self) -> dict:
        raise NotImplementedError("Information has not been implemented.")
