import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True


    bot = commands.Bot(command_prefix="!", intents = intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (bot.user.id)")
        print(bot.user)
        print(bot.user.id)
        print("__________________________")

    
    
    @bot.command()

    async def ping(ctx):
        """Answers with Pong"""
        await ctx.send("pong")

        
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)







if __name__ == "__main__":
    run()


