from discord.ext import commands


class OwnerCog(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='purge', aliases=['clean', 'del', 'delete'])
    @commands.is_owner()
    async def purge(self, ctx, amount=None):
        if amount is None:
            await ctx.channel.purge(limit=6)
        # Too dangerous for ordinary mortals
        # elif amount == "all":
        #     await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=int(amount) + 1)
            
def setup(bot):
    bot.add_cog(OwnerCog(bot))
    print('Owner Setup')
