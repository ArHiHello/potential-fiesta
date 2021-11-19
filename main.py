import discord
from discord.ext import commands
from websever import keep_alive

client = commands.Bot(command_prefix='?')

client.command()
async def hi(ctx):
  await ctx.send('HELLO')

keep_alive()
  
client.run('ODU1MTM2NTI5NDk1ODgzODI3.YMuF9A.27-z-UWzMlN0x2kFILja5uJoudw')
