import discord
from discord.ext import commands

class NotOwner(commands.CheckFailure):
    ...


def is_owner():
    async def predicate(ctx):
        if ctx.author.id != ctx.guild.owner_id:
            raise NotOwner("You do not have permission")
        return True
    return commands.check(predicate)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="#", intents=intents)

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_owner()
    async def load(ctx, cog: str):
        await bot.load_extension(f'cogs.{cog.lower()}')

    @commands.command()
    @is_owner()
    async def unload(ctx, cog: str):
        await bot.unload_extension(f'cogs.{cog.lower()}')

    @commands.command()
    @is_owner()
    async def reload(ctx, cog: str):
        await bot.reload_extension(f'cogs.{cog.lower()}')

    @commands.command()
    @is_owner()
    async def kyle(self, ctx):
        await ctx.send("Kyle is a Pervert who preys on all girls.")

# Error Handleing 

    @load.error
    async def load_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")

    @unload.error
    async def unload_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")

    @reload.error
    async def reload_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")

    @kyle.error
    async def kyle_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied")

async def setup(bot):
    await bot.add_cog(Admin(bot))