from ModuleBase import ModuleBase
from discord.ext import commands
from enum import Enum, auto
import re

class SearchStatus(Enum):
    ONGOING = auto()
    CANCELLED = auto()


class Search(ModuleBase):
    """
    A module for searching through messages with regular expressions.

    Attributes:
        bot: Bot this module is attached to.
        active_searches: a dict mapping the 'cancel message' to a flag which determines whether the search has been cancelled.
    """


    def __init__(self, bot):
        self.bot = bot
        self.active_searches = {}
        self.bot.on_reaction_add = self.bot.event(self.on_reaction_add)


    # TODO: the docstring doesn't display correctly in !help search.
    @commands.command()
    async def search(self, ctx, regex: str):
        """
        Find all messages in the current channel matching a regex.

        Args:
            regex: regular expression.
        """

        # The pattern must be enclosed in backticks, enforcing this means we don't have to manually escape most special characters.
        if len(regex) < 2 or regex[0] != "`" or regex[-1] != "`":
            await ctx.send("The pattern must be enclosed in backticks: \\`pattern\\`.")
            return
        else:
            regex = regex[1:len(regex)-1]
        
        await (cancel_message := await ctx.send("Searching; react with :x: to cancel.")).add_reaction("\u274c")
        
        self.active_searches[cancel_message] = SearchStatus.ONGOING

        match_count = 0
        async for message in ctx.channel.history(oldest_first=True):
            if self.active_searches[cancel_message] == SearchStatus.CANCELLED:
                await ctx.send("Search cancelled.", reference=cancel_message, mention_author=False)
                break

            # Ignore bot's own messages when this command was issued.
            if message not in [ctx.message, cancel_message] and (match := re.search(regex, message.content)):
                # Cannot send back an empty message, so we ignore empty matches.
                if len(match.group(0)):
                    match_count += 1
                    # Send only the full match, ignore sub-matches.
                    await ctx.send(match.group(0), reference=message, mention_author=False)
        else:
            await ctx.send(
                "Done, {} {}.".format( 
                    match_count if match_count else "no",
                    "result" if match_count == 1 else "results"
                )
            )

        del self.active_searches[cancel_message]


    # Cancel a search with a reaction.
    async def on_reaction_add(self, reaction, user):
        if user != self.bot.user and reaction.emoji == "\u274c":
            if reaction.message in self.active_searches:
                self.active_searches[reaction.message] = SearchStatus.CANCELLED


    @staticmethod
    def getInformation() -> dict:
        # TODO
        return {}
    


async def setup(bot):
    await bot.add_cog(Search(bot))
