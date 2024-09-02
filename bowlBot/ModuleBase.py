import logging
import json


from discord.ext import commands


class ModuleBase(commands.Cog):
    MODULE_REGISTRY = []

    def __init_subclass__(cls, **kwargs):
        super.__init_subclass__(**kwargs)
        cls.MODULE_REGISTRY.append(cls)
        # Create a logger and add handler + formatter
        cls.logger: logging.Logger = logging.getLogger(cls.__name__)
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(levelname)s - %(asctime)s]: [Module -> %(name)s, File -> %(module)s, Function -> %(funcName)s] %(message)s"
        )
        ch.setFormatter(formatter)
        cls.logger.addHandler(ch)

        file = open("config.json")
        moduleDict = json.load(file)
        level: int = logging.WARNING
        for module, conditions in moduleDict["modules"].items():
            # print(module, conditions)
            print(module.split(".")[-1])
            print(cls.__name__)
            if module.split(".")[-1] == cls.__name__:
                level = conditions["logLevel"]
                print(level)
        cls.logger.setLevel(level)

    def getInformation(self) -> dict:
        raise NotImplementedError("Information has not been implemented.")
