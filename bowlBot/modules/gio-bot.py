from ModuleBase import ModuleBase
from discord.ext import commands
import discord
import re

class ModuleIndex(ModuleBase):
    def __init__(self, bot):
        self.bot = bot  
    @commands.command()
    async def on_message(message):
      goodnight_images=["C:\Users\NANDA KISHORE REDDY\Desktop\botbowl\bowlBot\bowlBot\modules\gio saab/gio1.png","C:\Users\NANDA KISHORE REDDY\Desktop\botbowl\bowlBot\bowlBot\modules\gio saab/gio2.png","C:\Users\NANDA KISHORE REDDY\Desktop\botbowl\bowlBot\bowlBot\modules\gio saab/gio3.png","C:\Users\NANDA KISHORE REDDY\Desktop\botbowl\bowlBot\bowlBot\modules\gio saab/gio4.png"]
      if re.search(r"gn|good night|hit sack", message.content.lower()):
        for image in goodnight_images:
          await message.channel.send(image)
async def setup(bot):
    await bot.add_cog(gio-bot(bot))




