import lightbulb
import hikari
import discord
from stockx import search
from hikari.channels import ChannelType

bot = lightbulb.BotApp(
    token = "MTAyMDM5OTU0ODQ2MTQ4NjIwMA.GWUkNs.nGxLO-vLPOnIxhWSBNJ2vPOVJckXANAptJFTfQ",
    default_enabled_guilds=("786976921824788480")
)

channel_id = "1020407319089131624"

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started!')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command()
@lightbulb.option("item", "Item to find")
@lightbulb.command("stockx", "Searchs StockX for a specific item")
@lightbulb.implements(lightbulb.SlashCommand)
async def stockx(message: lightbulb.Context) -> None:
   # await ctx.respond(ctx.options.text)   
    
    query = message.options.text
    print("searching...")
    item = search(query)
    print("item found")
    print("printing embeds")


    embed = discord.Embed(
        title=item['title'],
        url='https://stockx.com/' + item['urlKey']
    )
    embed.set_thumbnail(
        url=item['media']['imageUrl']
    )
    embed.add_field(
        name='Colorway',
        value=item['colorway']
    )
    embed.add_field(
        name='Style ID',
        value=item['styleId']
    )
    embed.add_field(
        name='Last Sale',
        value=item['market']['lastSale']
    )
    await message.respond(embed=embed)

bot.run()
