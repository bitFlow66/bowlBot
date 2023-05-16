from ModuleBase import ModuleBase
from discord.ext import commands
import discord
import re
import os
import random

from os import listdir
from os.path import isfile, join

class gioBot(ModuleBase):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener("on_message")
    async def goodnight(self,message):
        if re.search(r"gn|good night|sack|goodnight", message.content.lower()):
            filePath="modules/gioBot/images/"
            goodnight_images= [join(filePath,f) for f in listdir(filePath) if isfile(join(filePath,f))]
            path=random.choice(goodnight_images)
            with open(path, 'rb') as byteP:
                picture = discord.File(byteP)
                await message.channel.send(file=picture)
async def setup(bot):
    await bot.add_cog(gioBot(bot))







