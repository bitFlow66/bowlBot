from discord.ext import commands
import json
import os


class BowlBot(commands.Bot):
    def __init__(self, intents):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        await self.loadModules()

        print("Bot is ready!")

    async def loadModules(self):
        """
        Loads all modules specified in config.json
        """
        file = open("config.json")
        moduleDict = json.load(file)
        for module, condition in moduleDict["modules"].items():
            if condition:
                await self.load_extension(module)
