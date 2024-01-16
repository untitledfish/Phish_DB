import discord
from discord.ext import commands
from discord import Interaction 

client = commands.Bot(command_prefix = "*", intents = discord.Intents.all())

@client.event
async def on_ready():
    # set client activity and status
    await client.change_presence(activity = discord.activity.Game(name = 
                "fucking fish"), status = discord.Status.do_not_disturb)
    print(f"{client.user.name} is bouta cum")

@client.command() # a list of help options for when people are retarded
async def helpme(ctx):
    await ctx.send("okay dumbass, here's what I do:\n\n"
            "*hello - greets new people correctly\n"
            "*ping - pong!")

@client.command() # this is how you greet people in phish tank
async def hello(ctx):
    await ctx.send("auto's first wet dream was gay")

@client.command()
async def ping(ctx):
    bot_latency = round(client.latency*1000)
    await ctx.send(f"Pong!... {bot_latency}ms")

# shit don't work but it's fine i didn't want slash commands anyway
#@client.tree.command(name = "ping", description = "pong")
#async def ping(interaction : Interaction):
 #   bot_latency = round(client.latency*1000)
 #   await interaction.response.send_message(f"Pong!... {bot_latency}ms")

client.run("MTE5NjkzMzQ5MTI2MzI5MTQ4Mw.GD2uL6.kOxkRiGcXpanguH4YDkUQBJE-dnwSB-HYhzSTE")

