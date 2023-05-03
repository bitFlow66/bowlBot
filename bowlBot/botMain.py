
def main():
    import os

    import discord
    from dotenv import load_dotenv

    from BowlBot import BowlBot

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = BowlBot(discord.Intents.all())

    bot.run(TOKEN)


if __name__ == "__main__":
    main()
