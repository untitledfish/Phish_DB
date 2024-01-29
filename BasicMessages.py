from main import client
import os
import discord
from discord.ext import commands
from discord import Interaction 

@client.command() # a list of help options for when people are retarded
async def help(ctx):
    await ctx.send("okay, here's what I do:\n\n"
            "My prefix is '*' (as you already knew to get here)\n\n"
            "hello - greets new people appropriately\n"
            "ping - pong!")

@client.command() # this is how you greet people in phish tank
async def hello(ctx):
    await ctx.send("auto's first wet dream was gay")

@client.command() # basic ping getter
async def ping(ctx):
    bot_latency = round(client.latency*1000)
    await ctx.send(f"Pong!... {bot_latency}ms")