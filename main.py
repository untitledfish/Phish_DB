import os
import discord
import Dtoken
from discord.ext import commands
from discord import Interaction 

client = commands.Bot(command_prefix="*", intents=discord.Intents.all(), help_command=None)
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
    # set client activity and status
    await client.change_presence(activity=discord.activity.Game(name = 
                "fucking a fish"), status=discord.Status.do_not_disturb)
    print(f"{client.user.name} is bouta cum") # this bot edges constantly

client.run(Dtoken.TOKEN)

