import settings
import random
import discord
import time
from discord.ext import commands
from cogs.greetings import Greetings
from cogs.admin import Admin
from cogs.music import Music

# ------------------------------------------------------------------

logger = settings.logging.getLogger("bot")


# Bot start command
def run():
    intents = discord.Intents.all()
    intents.message_content = True

    bot = commands.Bot(command_prefix="#", intents=intents)

    bot.remove_command("help")

    # Turns bot on and sets up logging
    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id})')

        for cmd_file in settings.COMMANDS_DIR.glob("*.py"):
            if cmd_file.name !="__init__.py":
                await bot.load_extension(f'bot_commands.{cmd_file.name[:-3]}')

        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file.name !="__init__.py":
                await bot.load_extension(f'cogs.{cog_file.name[:-3]}') 


# Global Error Handleing
    @bot.event
    async def on_command_error(ctx, error): 
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("handled error globally")

    # @bot.event
    # async def on_message(message):
    #     time.sleep(5)
    #     await message.delete()

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()