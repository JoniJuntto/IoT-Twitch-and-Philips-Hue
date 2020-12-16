from twitchio.ext import commands

from philipsHue import bomb
from philipsHue import fbi
from philipsHue import lightsOn

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:XXXXXX', client_id='XXXXXX',
                         nick='kiukkuDoggo', prefix='!',
                         initial_channels=['huikkastriimi'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        await self.event_message(message)

    @commands.command(name='FBI')
    async def fbi(self, ctx):
        await ctx.send(f'VALOT POIS, ja kaikki piiloon!')
        fbi()

    @commands.command(name='pommi')
    async def pommi(self, ctx):
        await ctx.send(f'{ctx.author.name} has planted the bomb!')
        bomb()
        lightsOn()

    @commands.command(name='valot')
    async def valot(self, ctx):
        await ctx.send(f'Tulkoon valo!')
        lightsOn()


bot = Bot()
bot.run()

if __name__ == '__main__':
    bot.run()
