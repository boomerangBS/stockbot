#import
#https://discord.com/api/oauth2/authorize?client_id=1019625684471124099&permissions=277025507392&scope=bot%20applications.commands

import discord,os,random,discord_slash,datetime,requests,finnhub
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option,create_choice
from discord.utils import get
from discord.ext import commands,tasks
from life import *


intents = discord.Intents().default()
intents.members = True
bot = commands.Bot(command_prefix="?", description="bot in dev")
slash = SlashCommand(bot,sync_commands=True)
key2=os.environ["api_key2"]
key1=os.environ["api_key"]
finnhub_client = finnhub.Client(api_key=key1)

print("starting...")

@slash.slash(name="ping",description="Online ?",)
async def ping(ctx):
  await ctx.send(f"pong {ctx.author.mention}")

@slash.slash(name="Monitoring_Page")
async def Monitoring_Page(ctx):
  await ctx.send("link")

@bot.command()
async def ping(ctx):
  await ctx.send(f"pong {ctx.author.mention}")

@slash.slash(name="Stock_price",description="Give to you the price off a stock",options = [ 
create_option(name="name",description="Name of the stock",option_type = 3,required=True)])
async def price(ctx,name):
  try:
    
   result=requests.get(f"https://financialmodelingprep.com/api/v3/quote-short/{name}?apikey={key2}").json()
   embed=discord.Embed(title=f"{name}'s stock price",description=f"Here is the price and volume of {name}'s stock \n disclaimer : https://bit.ly/SBotD")
   embed.set_thumbnail(url="https://www.generationcyb.net/wp-content/uploads/2022/03/stonks-meme.jpg")
   embed.add_field(name="price",value=result[0]["price"])
   embed.add_field(name="volume",value=result[0]["volume"])
   await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title="Error",description="We can't found this stock!")
    embed.set_thumbnail(url="https://i.imgflip.com/35a1ly.jpg?a462480")
   
    await ctx.send(embed=embed)
 
@bot.command()
async def price(ctx,name):
  try:
    
   result=requests.get(f"https://financialmodelingprep.com/api/v3/quote-short/{name}?apikey={key2}").json()
   embed=discord.Embed(title=f"{name}'s stock price",description=f"Here is the price and volume of {name}'s stock")
   embed.set_thumbnail(url="https://www.generationcyb.net/wp-content/uploads/2022/03/stonks-meme.jpg")
   embed.add_field(name="price",value=result[0]["price"])
   embed.add_field(name="volume",value=result[0]["volume"])
   await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title="Error",description="We can't found this stock!")
    embed.set_thumbnail(url="https://i.imgflip.com/35a1ly.jpg?a462480")
   
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("started!")
    print("bot ready !")
keep_alive()  
bot.run(os.environ["token"])