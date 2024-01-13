import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = ""
        self.text_channel_list = []
        self.set_message()

    def set_message(self):
        self.help_message = """
```
General commands:
#help - displays all available commands
#p <keyword> - finds the song on youtube and plays it in yor currrent channel
#q - displays the current music queue
#skip - skips the current song being played
#clear - clears the queue
#leave - discoonects the bot from vc
#pause - pauses song
#resume - resumes song
```
"""


    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(f"type {self.bot.command_prefix}help"))


    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="help", help="Displayes all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

async def setup(bot):
    await bot.add_cog(Help(bot))