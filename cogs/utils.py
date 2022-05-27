from discord.ext import commands

class UtilsCog(commands.Cog, name="Utils Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='purge', aliases=['clean', 'del', 'delete'])
    async def purge(self, ctx, amount=None):
        if amount is None:
            await ctx.channel.purge(limit=6)
        # Too dangerous for ordinary mortals
        # elif amount == "all":
        #     await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=int(amount) + 1)

def setup(bot):
    bot.add_cog(UtilsCog(bot))
    print('Utils Setup')
