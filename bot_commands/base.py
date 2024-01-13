from discord.ext import commands

@commands.group()
async def base(ctx):
     if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} does not belong to math')

@base.command()
async def Kyle(ctx):
    await ctx.send("Kyle is a Pervert who preys on all girls.")

async def setup(bot):
    bot.add_command(base)