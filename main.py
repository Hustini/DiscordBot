import inspect
import os
import discord
import dotenv
from discord.commands import Option
from discord.ext import commands


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(intents=intents, command_prefix='$', debug_guilds=[1215352459296243783])

    @bot.event
    async def on_ready():
        print(f'{bot.user} ready')

    @bot.command()  # says hello
    async def hello(ctx):
        frame = inspect.currentframe()
        print(f'{frame.f_code.co_name} called')
        await ctx.send('Hello')

    @bot.slash_command()  # greets member
    async def greet(ctx, user: Option(discord.Member)):
        await ctx.respond(f'Hallo {user.mention}')

    @bot.command()
    async def join(ctx):
        channel = ctx.author.voice.channel
        print(f'{channel} joined')
        await channel.connect()

    @bot.command()
    async def leave(ctx):
        channel = ctx.author.voice.channel
        print(f'{channel} left')
        await ctx.voice_client.disconnect()

    dotenv.load_dotenv()
    token = str(os.getenv("TOKEN"))
    bot.run(token)


if __name__ == '__main__':
    main()
