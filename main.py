#import
import discord,os,random,discord_slash,datetime,requests,finnhub
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option,create_choice
from discord.utils import get
from discord.ext import commands,tasks
intents = discord.Intents().default()
intents.members = True
bot = commands.Bot(command_prefix="?", description="bot in dev")
slash = SlashCommand(bot,sync_commands=True)
key2=os.environ["api_key2"]
key1=os.environ["api_key"]
finnhub_client = finnhub.Client(api_key=key1)

print("starting...")




@bot.command()
async def test(ctx):
  await ctx.send(f"je repond au test de {ctx.author.mention}")

@bot.command()
async def price(ctx,*,arg="AAPL"):
  try: 
   result=requests.get(f"https://financialmodelingprep.com/api/v3/quote-short/{arg}?apikey={key2}").json()
   embed=discord.Embed(title=f"{arg}'s stock price",description=f"Here is the price and volume of {arg}'s stock")
   embed.set_thumbnail(url="https://www.generationcyb.net/wp-content/uploads/2022/03/stonks-meme.jpg")
   embed.add_field(name="price",value=result[0]["price"])
   embed.add_field(name="volume",value=result[0]["volume"])
   await ctx.send(embed=embed)
  except:
    await ctx.send("error: not found")

  
@bot.command()
async def search(ctx,*title):
  found=finnhub_client.symbol_lookup(title)
  embed=discord.Embed(title="**search result**",description="here is the result of your search")
  embed.set_thumbnail(url="https://www.my-medical.fr/12905-large_default/loupe-ronde-grossissement-x5-my-medical.webp")
  found1=found["result"][1]["symbol"],found["result"][1]["description"]
  found2=found["result"][2]["symbol"],found["result"][2]["description"]
  found3=found["result"][3]["symbol"],found["result"][3]["description"]
  found4=found["result"][4]["symbol"],found["result"][4]["description"]
  found5=found["result"][5]["symbol"],found["result"][5]["description"]
  embed.add_field(name="1",value=found1)
  embed.add_field(name="2",value=found2)
  embed.add_field(name="3",value=found3)
  embed.add_field(name="4",value=found4)
  await ctx.send(embed=embed)
  
  


@bot.event
async def on_ready():
    print("started!")
    print("bot ready !")
  
bot.run(os.environ["token"])