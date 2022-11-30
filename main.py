import os
import discord
from discord.ext import commands
import numpy as np
import random
import requests

import sys

import psutil #import Processs, virtual_memory
import lib_platform #import python_version
from discord import __version__ as discord_version
from time import time

# from keep_alive import keep_alive

token = ("OTg3MzkxODM2ODg2Nzk0MjYw.Gx714y.O2PQMNoRSYjUo7-QwhL1BitW3Mhe0ycIL5ldMw")

client = commands.Bot(command_prefix='yar ')
client.remove_command("help")


@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client))
    activity = discord.Game(name="yar help", type=3)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)


########################################################################################################
#Help commands


@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        url=
        "https://discord.com/api/oauth2/authorize?client_id=987391836886794260&permissions=122406693952&scope=bot",
        color=0xF49726)
    embed.add_field(
        name="Command Categories :",
        value="🐸 `memes     :` Image generation with a memey twist.\n" +
        "🎲 `random    :` Just some random stuff\n" +
        "🤗 `emotion   :` Share Your Emotion\n" +
        "🌚 `fun       :` Entertainment! **Bus Thoda Sambhal Ke**\n" +
        "🔧 `utility   :` Bot utility zone\n\n" +
        "To view the commands of a category, send `yar help <category>`\n\n--[Add the Bot](https://discord.com/api/oauth2/authorize?client_id=987391836886794260&permissions=122406693952&scope=bot) --  --[Join the community](https://discord.gg/83Kx5FP5sf) --",
        inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Help requested by: {}".format(
                         ctx.author.display_name))

    await ctx.send(embed=embed)


@help.command()
async def memes(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **meme** \n`yar meme     :` Complet Dsei Memes\n`yar vmeme    :` Get Memes In Video\n`yar dank     :` Desi Dank Memes\n`yar engdank  :` English Dank Memes\n`yar animeme  :` Anime Memes\n`yar nsmeme   :` **NSFW**  Memes\n`yar bakchodi :` Bakchodi",
        color=0xF49726)
    embed.add_field(name="\nThere r many memes which can trigged you 😬",
                    value="`So ,Sorry in Advance`",
                    inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **fun** \nIt contain NSFW content,**Tu Thoda Sambhal Ke** **NSFW**\n||`yar tites       :` Randome Tites Images\n`yar desitites   :` Only Desi Tits\n`yar blowjob     :` Blowjob\n`yar randomnsfw  :` Random NSFW Content\n`yar waifu       :` Wsifu \n`yar neko        :` Neko\n`yar trap        :` Something\n`yar aniblowjob  :`Anime Blowjob||",
        color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@help.command()
async def random(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **random** \n`yar animals    :` Get Animals Pics\n`yar aww        :` Awwwwwwwwwwwww\n`yar foodporn   :` Foodporn ,**Vah Nahi Hai Jo TU Samajh Raha Hai**\n`yar shayari    :` Shayari\n`yar aniquote   :` Anime Quote\n`yar hi         :`\n`yar hello      :`",
        color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


# @help.command()
# async def fantasy(ctx):
#     embed = discord.Embed(
#         title="IndianDesiMemer Help Center ✨",
#         description=
#         "Commands of **fantasy** \nIt contain NSFW content,**Tu Thoda Sambhal Ke** **NSFW**\n||`yar wsifu       :` Wsifu \n`yar neko        :` Neko\n`yar teap        :` Something\n`yar aniblowjob  :`Anime Blowjob||",
#         color=0xF49726)
#     embed.set_footer(icon_url=ctx.author.avatar_url,
#                      text="Command requested by: {}".format(
#                          ctx.author.display_name))
#     await ctx.send(embed=embed)


@help.command()
async def emotion(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **emotions** \n`yar blush       :`\n`yar cry         :`\n`yar sleepy      :`\n`yar thumbsup    :`\n`yar thinking    :`\n`yar triggered   :`\n`yar happy       :`",
        color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@help.command()
async def utility(ctx):
    embed = discord.Embed(title="IndianDesiMemer Help Center ✨",
                          description="Commands of **utility** \n`yar ping      :`\n`yar stats     :`\n`yar guildlink  :`",
                          color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


########################################################


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            "**Ruko Zara Sabar Karo**\n ⚠ `{0} second` baad try karna ⚠".
            format(round(error.retry_after, 2)))


##############################################################


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def meme(ctx):
    memeLink = [
        "desimemes", "subtleindiantraits", "DesiAdultMemesCaption",
        "DankIndianMeme", "IndianDankMemes", "dankinindia", "HindiMemes",
        "IndianMeyMeys", "IndianMemeTemplates", "IndianDankTemplates",
        "FingMemes"
    ]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            np.random.choice(memeLink) + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    subreddit = (m["subreddit"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍\t" + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def vmeme(ctx):
    list_of_vmemes = [
        "https://www.reddit.com/r/IndianDankMemes/comments/qk7lp7",
        "https://www.reddit.com/r/IndianDankMemes/comments/qdahkc",
        "https://www.reddit.com/r/IndianDankMemes/comments/qn8giy",
        "https://www.reddit.com/r/IndianDankMemes/comments/raufw2",
        "https://www.reddit.com/r/IndianDankMemes/comments/rux4cr",
        "https://www.reddit.com/r/IndianDankMemes/comments/ppsl18",
        "https://www.reddit.com/r/IndianDankMemes/comments/p4n195",
        "https://www.reddit.com/r/IndianDankMemes/comments/pcky98",
        "https://www.reddit.com/r/IndianDankMemes/comments/pml8g6",
        "https://www.reddit.com/r/IndianDankMemes/comments/vcr56w",
        "https://www.reddit.com/r/IndianDankMemes/comments/v59i4s",
        "https://www.reddit.com/r/IndianDankMemes/comments/uvrmsa",
        "https://www.reddit.com/r/IndianDankMemes/comments/v2bfef",
        "https://www.reddit.com/r/IndianDankMemes/comments/v8yo68",
        "https://www.reddit.com/r/IndianDankMemes/comments/vfm6zl",
        "https://www.reddit.com/r/IndianDankMemes/comments/vh5qfb",
        "https://www.reddit.com/r/IndianDankMemes/comments/v275cy",
        "https://www.reddit.com/r/IndianDankMemes/comments/v4hvrz",
        "https://www.reddit.com/r/IndianDankMemes/comments/v30sgp",
        "https://www.reddit.com/r/IndianDankMemes/comments/vb3g6g",
        "https://www.reddit.com/r/IndianDankMemes/comments/v8ciq9",
        "https://www.reddit.com/r/IndianDankMemes/comments/uzmtd0",
        "https://www.reddit.com/r/IndianDankMemes/comments/v7g3ub",
        "https://www.reddit.com/r/IndianDankMemes/comments/vftzrd",
        "https://www.reddit.com/r/IndianDankMemes/comments/vcolnw",
        "https://www.reddit.com/r/IndianDankMemes/comments/ve6yoy",
        "https://www.reddit.com/r/IndianDankMemes/comments/v3b52h",
        "https://www.reddit.com/r/IndianDankMemes/comments/uxewox",
        "https://www.reddit.com/r/IndianDankMemes/comments/v327al",
        "https://www.reddit.com/r/IndianDankMemes/comments/v5lifg",
        "https://www.reddit.com/r/IndianDankMemes/comments/vgpcvc",
        "https://www.reddit.com/r/IndianDankMemes/comments/v1umj4",
        "https://www.reddit.com/r/IndianDankMemes/comments/vf1l8g",
        "https://www.reddit.com/r/IndianDankMemes/comments/v0z7pm",
        "https://www.reddit.com/r/IndianDankMemes/comments/vcomlj",
        "https://www.reddit.com/r/IndianDankMemes/comments/vdctmd",
        "https://www.reddit.com/r/IndianDankMemes/comments/v5fsjr",
        "https://www.reddit.com/r/IndianDankMemes/comments/v06puc",
        "https://www.reddit.com/r/IndianDankMemes/comments/v074wx",
        "https://www.reddit.com/r/IndianDankMemes/comments/v57hki",
        "https://www.reddit.com/r/IndianDankMemes/comments/v0bz81",
        "https://www.reddit.com/r/IndianDankMemes/comments/v1olga",
        "https://www.reddit.com/r/IndianDankMemes/comments/vdio5r",
        "https://www.reddit.com/r/IndianDankMemes/comments/v07074",
        "https://www.reddit.com/r/IndianDankMemes/comments/v9b435",
        "https://www.reddit.com/r/IndianDankMemes/comments/vbzhn9",
        "https://www.reddit.com/r/IndianDankMemes/comments/vgp85p",
        "https://www.reddit.com/r/IndianDankMemes/comments/v29mzg",
        "https://www.reddit.com/r/IndianDankMemes/comments/v8y11r",
        "https://www.reddit.com/r/IndianDankMemes/comments/uwg9ta",
        "https://www.reddit.com/r/dankinindia/comments/v1i2am",
        "https://www.reddit.com/r/dankinindia/comments/v63ou1",
        "https://www.reddit.com/r/dankinindia/comments/v2by9b",
        "https://www.reddit.com/r/dankinindia/comments/v7n7qp",
        "https://www.reddit.com/r/dankinindia/comments/v7ip9q",
        "https://www.reddit.com/r/dankinindia/comments/v3sbl4",
        "https://www.reddit.com/r/dankinindia/comments/vaf1mx",
        "https://www.reddit.com/r/dankinindia/comments/v59her",
        "https://www.reddit.com/r/dankinindia/comments/v26r4v",
        "https://www.reddit.com/r/dankinindia/comments/v47b4i",
        "https://www.reddit.com/r/dankinindia/comments/uvx0gb",
        "https://www.reddit.com/r/dankinindia/comments/uzfura",
        "https://www.reddit.com/r/dankinindia/comments/vh9ot3",
        "https://www.reddit.com/r/dankinindia/comments/v752ni",
        "https://www.reddit.com/r/dankinindia/comments/uzpoaf",
        "https://www.reddit.com/r/dankinindia/comments/vh8c95",
        "https://www.reddit.com/r/dankinindia/comments/vhbyk7",
        "https://www.reddit.com/r/dankinindia/comments/vh7s9c",
        "https://www.reddit.com/r/dankinindia/comments/vhd9t1",
        "https://www.reddit.com/r/dankinindia/comments/vh5d7k",
        "https://www.reddit.com/r/dankinindia/comments/vh69ne",
        "https://www.reddit.com/r/dankinindia/comments/vh6tt3",
        "https://www.reddit.com/r/dankinindia/comments/vhbgt3",
        "https://www.reddit.com/r/dankinindia/comments/vh8y4k",
        "https://www.reddit.com/r/dankinindia/comments/vhdpn0",
        "https://www.reddit.com/r/dankinindia/comments/vh8tt0",
        "https://www.reddit.com/r/dankinindia/comments/vhus44",
        "https://www.reddit.com/r/dankinindia/comments/vh79b9",
        "https://www.reddit.com/r/dankinindia/comments/vhfrpm",
        "https://www.reddit.com/r/dankinindia/comments/vhei7z",
        "https://www.reddit.com/r/dankinindia/comments/vhfp8y",
        "https://www.reddit.com/r/dankinindia/comments/vhf4eh",
        "https://www.reddit.com/r/dankinindia/comments/vhiecd",
        "https://www.reddit.com/r/dankinindia/comments/vhi022",
        "https://www.reddit.com/r/dankinindia/comments/vhglgs",
        "https://www.reddit.com/r/dankinindia/comments/vhmiia",
        "https://www.reddit.com/r/FingMemes/comments/v4fo0w",
        "https://www.reddit.com/r/FingMemes/comments/v6p3bb",
        "https://www.reddit.com/r/FingMemes/comments/v2c8ek",
        "https://www.reddit.com/r/FingMemes/comments/v9tkr9",
        "https://www.reddit.com/r/FingMemes/comments/v4hyoe",
        "https://www.reddit.com/r/FingMemes/comments/vbvhj4",
        "https://www.reddit.com/r/FingMemes/comments/v4onuw",
        "https://www.reddit.com/r/FingMemes/comments/v5qq1r",
        "https://www.reddit.com/r/FingMemes/comments/v29x1p",
        "https://www.reddit.com/r/FingMemes/comments/v59knw",
        "https://www.reddit.com/r/FingMemes/comments/v6mx0h",
        "https://www.reddit.com/r/FingMemes/comments/vclz0l",
        "https://www.reddit.com/r/FingMemes/comments/vdjivb",
        "https://www.reddit.com/r/FingMemes/comments/vc0zcm",
    ]
    await ctx.send(np.random.choice(list_of_vmemes))


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def dank(ctx):
    memeLink = [
        "DankIndianMeme", "IndianDankMemes", "DankIndianMeme",
        "NSFW_IndianMemes" + "?t=all?hot"
    ]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            np.random.choice(memeLink))
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍" + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def engdank(ctx):
    # memeLink = ["desimemes","subtleindiantraits","DesiAdultMemesCaption","DankIndianMeme"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            "dankmemes" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍" + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def animeme(ctx):
    memeLink = ["animememes", "AnimeFunny", "Animemes", "goodanimemes"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            np.random.choice(memeLink) + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍" + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def nsmeme(ctx):
    memeLink = ["NSFWmemes", "NSFW_IndianMemes"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            np.random.choice(memeLink) + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍" + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def bakchodi(ctx):
    # memeLink = ["desimemes","subtleindiantraits","DesiAdultMemesCaption","DankIndianMeme"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/bakchodi" +
                            "?t=all?hotr")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍" + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


##########################################################################################################
@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def tites(ctx):
  if ctx.channel.is_nsfw():
    memeLink = ["tits","BreedingMaterial","hugeboobs","BigBoobsGW"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/"+np.random.choice(memeLink)+"?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl =  (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed=discord.Embed(title= title, url=postLink,color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by: {}  😏 ".format(ctx.author.display_name)+ "  By :r/"+subreddit)
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def desitites(ctx):
  if ctx.channel.is_nsfw():
#     memeLink = ["tits","BreedingMaterial","hugeboobs","BigBoobsGW"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/"+"indianboobs"+"?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl =  (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed=discord.Embed(title= title, url=postLink,color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by: {}  😏 ".format(ctx.author.display_name)+ "  By :r/"+subreddit)
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def blowjob(ctx):
  if ctx.channel.is_nsfw():
#     memeLink = ["tits","BreedingMaterial","hugeboobs","BigBoobsGW"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +"BlowJob" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl =  (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed=discord.Embed(title= title, url=postLink,color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by: {}  😏 ".format(ctx.author.display_name)+ "  By :r/"+subreddit)
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def randomnsfw(ctx):
  if ctx.channel.is_nsfw():
#     memeLink = ["tits","BreedingMaterial","hugeboobs","BigBoobsGW"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" + "BreedingMaterial" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl =  (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed=discord.Embed(title= title, url=postLink,color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by: {}  😏 ".format(ctx.author.display_name)+ "  By :r/"+subreddit)
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !") 

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def waifu(ctx):
  if ctx.channel.is_nsfw():
#     memeLink = ["tits","BreedingMaterial","hugeboobs","BigBoobsGW"]
    response = requests.get("https://api.waifu.pics/nsfw/waifu")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url, text="Requested by: {}  😏".format(ctx.author.display_name))
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")    

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def neko(ctx):
  if ctx.channel.is_nsfw():
    response = requests.get("https://api.waifu.pics/nsfw/neko")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url, text="Requested by: {}  😏".format(ctx.author.display_name))
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def trap(ctx):
  if ctx.channel.is_nsfw():
    response = requests.get("https://api.waifu.pics/nsfw/trap")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Requested by: {}  😏".format(ctx.author.display_name))
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.channel)
async def aniblowjob(ctx):
  if ctx.channel.is_nsfw():
    response = requests.get("https://api.waifu.pics/nsfw/blowjob")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url, text="Requested by: {}  😏".format(ctx.author.display_name))
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"{ctx.author.mention} Harami Manas!.. You can use this command in a nsfw channel only !")



###########################################################################################################


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def animals(ctx):
    AnimalsLink = [
        "Animals", "AnimalsBeingDerps", "FunnyAnimals", "AnimalsBeingJerks"
    ]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            np.random.choice(AnimalsLink) + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="\n👍" + uv +
                     "  Requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def aww(ctx):
    response = requests.get("https://meme-api.herokuapp.com/gimme/aww" +
                            "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="\n👍" + uv +
                     "  Requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def foodporn(ctx):
    response = requests.get(
        "https://meme-api.herokuapp.com/gimme/IndianFoodPhotos" + "?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="\n👍" + uv +
                     "  Requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def shayari(ctx):
    response = requests.get("https://meme-api.herokuapp.com/gimme/Shayari" +
                            "?t=all")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="  Requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def aniquote(ctx):
    response = requests.get("https://animechan.vercel.app/api/random")
    m = response.json()
    anime = (m["anime"])
    character = (m["character"])
    quote = (m["quote"])

    embed = discord.Embed(title="Quote From : " + anime,
                          description="**Charater :** " + "**" + character +
                          "**" + "\n" + "**" + quote + "**",
                          color=0xF49726)

    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="  Requested by: {}  ".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def hi(ctx):
    stikers = [
        "https://cdn.discordapp.com/emojis/984161048863064136.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/984161072544112650.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/984161346402795590.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/984161183240171601.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/520245813465710613.gif?size=60&quality=lossless&size=40"
    ]
    await ctx.send("aur {0} kaise".format(ctx.message.author.name))
    await ctx.send(np.random.choice(stikers))


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def hello(ctx):
    stikers = [
        "https://cdn.discordapp.com/emojis/984161048863064136.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/984161072544112650.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/984161346402795590.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/984161183240171601.gif?size=60&quality=lossless&size=40",
        "https://cdn.discordapp.com/emojis/520245813465710613.gif?size=60&quality=lossless&size=40"
    ]
    await ctx.send("aur {0} kaise".format(ctx.message.author.name))
    await ctx.send(np.random.choice(stikers))


###########################################################################################################


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def blush(ctx):
    images = [
        "https://tenor.com/view/blush-blushy-hide-embarrassed-gif-14915694",
        "https://tenor.com/view/joey-tribbiani-friends-smile-ramzes19-scromnyaga-gif-12180398",
        "https://tenor.com/view/shy-embarrassed-patrick-star-oh-stop-hihihi-gif-16083044",
        "https://tenor.com/view/shy-blushing-gif-22858302",
        "https://tenor.com/view/tom-and-jerry-tom-blushing-shy-blush-gif-20367454",
        "https://tenor.com/view/janhvi-janhvi-kapoor-sweet-thats-so-sweet-cute-gif-20831172",
        "https://tenor.com/view/carry-minati-carry-minati-roast-ajeyn-agar-carry-ajey-gif-17327697",
        "https://tenor.com/view/shy-aww-shucks-goofy-bashful-gif-16177836",
        "https://tenor.com/view/karma-anime-blush-boy-gif-14841901",
        "https://tenor.com/view/marin-nervous-red-blush-anime-gif-25259190",
    ]
    text = [
        "**face is red~**", "**blushed!!** >///<",
        "**has turned into a tomato**", "**Ka Chehra Lal Ho Chuka Hai**",
        "**Sharma Gaya**"
    ]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def cry(ctx):
    images = [
        "https://tenor.com/view/sad-cry-crying-tears-broken-gif-15062040",
        "https://tenor.com/view/embarrassed-sad-cry-smile-im-fine-gif-14251203",
        "https://tenor.com/view/sad-crying-spiderman-cry-face-ugly-face-gif-5701170",
        "https://tenor.com/view/rainn-wilson-crying-tears-depressed-unhappy-gif-15679110",
        "https://tenor.com/view/mad-upset-ugly-cry-crying-gif-14754689",
        "https://tenor.com/view/tom-y-jerry-tom-and-jerry-meme-sad-cry-gif-18054267",
        "https://tenor.com/view/sad-blackish-anthony-anderson-tears-upset-gif-4988274",
        "https://tenor.com/view/carry-minati-ajey-nagar-indian-you-tuber-carry-minati-roast-carry-gif-17684580",
        "https://tenor.com/view/carry-minati-ajey-nagar-indian-you-tuber-carry-minati-roast-carry-gif-17684550",
        "https://tenor.com/view/cat-catcry-gif-19131995",
    ]
    text = [
        "**is crying...**", "**cries... :'c**", "**ro raha hai...**",
        "**ka आंखों में आंसू......:c**", "**:'c**"
    ]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def sleepy(ctx):
    images = [
        "https://tenor.com/view/sleepy-tired-sleep-nap-yawn-gif-3552811",
        "https://tenor.com/view/sushichaeng-reaction-tired-tired-af-sleepy-gif-21021085",
        "https://tenor.com/view/sleepy-kid-baby-cute-baby-cute-gif-16632759",
        "https://tenor.com/view/monkey-mojothemonkey-zzsoobn-monkey-sleep-sleepy-gif-22926696",
        "https://tenor.com/view/sleepy-baby-sleepy-babe-falling-asleep-fall-asleep-gif-25288703",
        "https://tenor.com/view/dog-sleepy-sleep-sleepover-gif-21120294",
        "https://tenor.com/view/sleep-sleepy-falling-asleep-gif-23724651",
        "https://tenor.com/view/sleepy-doze-off-subway-fall-tired-gif-16051472",
        "https://tenor.com/view/sleepy-sleepy-fall-tired-train-wasted-gif-12214869",
        "https://tenor.com/view/so-sleepy-wide-awake-cant-sleep-in-the-toilet-gif-15086876",
    ]
    text = [
        "**wants to sleep......**", "**needs a nap...**", "**is sleepy...**",
        "**सोना चाहता है......**", "**सोना चाहता है......तो मुंह बंद**"
    ]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def thumbsup(ctx):
    images = [
        "https://tenor.com/view/love-gif-24777608",
        "https://tenor.com/view/boy-kid-computer-thumbs-up-face-gif-9548945",
        "https://tenor.com/view/thumbs-up-good-great-excellent-like-gif-4987000",
        "https://tenor.com/view/rjumen-laugh-man-cool-nice-perfect-gif-23675313",
        "https://tenor.com/view/sponge-bob-thumbs-up-yes-gif-15389215",
        "https://tenor.com/view/carry-minati-ajey-nagar-indian-you-tuber-carry-minati-roast-carry-gif-17684636",
        "https://tenor.com/view/thumbs-up-double-thumbs-up-like-agreed-yup-gif-11663223",
        "https://tenor.com/view/thumbs-up-flipping-off-psycho-brooke-fake-flip-off-gif-14033162",
        "https://tenor.com/view/chicken-animated-dancing-chicken-dance-two-thumbs-up-gif-17525695",
    ]
    text = [
        "** agrees!**", "**has a thumbs up!**",
        "**gives a thumbs up!...........:**"
    ]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def thinking(ctx):
    images = [
        "https://tenor.com/view/batman-thinking-thinking-about-you-think-thinking-of-you-gif-20503421",
        "https://tenor.com/view/hmmm-thinking-confused-gif-14450462",
        "https://tenor.com/view/oh-thinking-stress-gif-15614592",
        "https://tenor.com/view/thinking-pensando-mmm-interesting-interesante-gif-14274248",
        "https://tenor.com/view/pensando-blackman-conta-black-nazare-gif-15088126",
        "https://tenor.com/view/meme-thinking-gif-23334820",
        "https://tenor.com/view/confused-math-what-wtf-peep-gif-6081931",
        "https://tenor.com/view/thinking-look-up-frowning-deep-thought-gif-14441239",
    ]
    text = [
        "**is thinking**", "**is thinking something......**",
        "**कुछ सोच रहा है......:**"
    ]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def triggered(ctx):
    images = [
        "https://tenor.com/view/hamster-triggered-rage-shaking-gif-17789643",
        "https://tenor.com/view/doge-meme-triggered-gif-24408595",
        "https://tenor.com/view/triggered-gif-14011990",
        "https://tenor.com/view/lebron-james-triggered-gif-24136846",
        "https://tenor.com/view/triggered-cat-gif-20356985",
        "https://tenor.com/view/krumpi-pikrum-foutre-trefou-maeva-gif-19327417",
        "https://tenor.com/view/memes-annoyed-face-gif-18141360",
        "https://tenor.com/view/meme-triggered-funny-face-laser-memes-gif-16215294",
    ]
    text = ["**is triggered!**"]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def happy(ctx):
    images = [
        "https://tenor.com/view/happy-happy-dog-dog-happiest-dog-super-happy-gif-17885812",
        "https://tenor.com/view/shaq-shimmy-gif-20800749",
        "https://tenor.com/view/raju-rastogi-3idot-3idiots-movie-crying-happily-tear-of-happiness-gif-23203465",
        "https://tenor.com/view/trollge-troll-troll-face-meme-horror-gif-24782665",
        "https://tenor.com/view/cat-happy-smile-happy-cat-happy-cat-meme-gif-24350154",
        "https://tenor.com/view/carry-minati-ajey-nagar-indian-you-tuber-carry-minati-roast-carry-gif-17684892",
        "https://tenor.com/view/carry-minati-ajey-nagar-indian-you-tuber-carry-minati-roast-carry-gif-17684169",
        "https://tenor.com/view/laugh-lol-happy-lmao-old-man-gif-17653940",
    ]
    text = ["**is happy!**", "**is......**"]
    await ctx.send('{0} '.format(ctx.author.display_name) +
                   np.random.choice(text))

    await ctx.send(np.random.choice(images))


############################################################################################################
# @client.command()
# @commands.cooldown(1, 5, commands.BucketType.user)
# async def rolldice(ctx):

#     text = [" :one:"," :two:"," :three:"," :four:"," :five:"," :six:",]
#     await ctx.send('{0}s'.format(ctx.author.display_name) +"\nNumber is"+
#                    np.random.choice(text))

#############################################################################################################


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx):
    await ctx.send('Ping! **{0}**ms'.format(round(client.latency * 1000)))
    await ctx.send(
        "Socha nahi tha koi yeh **command** use karega \n {0} Q".format(
            ctx.message.author.name))

    await ctx.send(
        "https://cdn.discordapp.com/emojis/986684266257743913.webp?size=60&quality=lossless&size=40"
    )




@client.command()
@commands.cooldown(1,900, commands.BucketType.user)
async def stats(ctx):
  
  
  start = time()
  latency = ('{0}ms'.format(round(client.latency * 1000)))
  end = time()
  response = ('{0}ms'.format(round(end-start) * 1000))

  
  system = sys.version

  
   
  embed = discord.Embed(
      title= "Server Information",
      color=0xF49726
    )
  
  embed.add_field(name="Bot Version", value = "0.0.12", inline=True)
  embed.add_field(name="System Version", value= system , inline=True)
  embed.add_field(name="Discord.py Version", value= discord_version , inline=True)
  embed.add_field(name="Available Memory", value= "{0}%".format(round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)), inline=True)
  embed.add_field(name="CPU Usage", value= "{0}%".format(psutil.cpu_percent(4)), inline=True)
  embed.add_field(name="RAM Usage", value= "{0}%".format(psutil.virtual_memory()[2]), inline=True)
  embed.add_field(name="Server Joined", value=str(len(client.guilds)), inline=True)
  embed.add_field(name="Latency", value= latency, inline=True)
  embed.add_field(name="Last Update", value="26 Jun 2022", inline=True)
  await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def link(ctx):
    embed = discord.Embed(
      title= "Click me to invite me to your server!",url = "https://discord.com/api/oauth2/authorize?client_id=987391836886794260&permissions=122406693952&scope=bot",
      color=0xF49726
    )
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def guildlink(ctx):
  await ctx.send("**💝| Come join our discord to ask for help or just have fun!**")
  await ctx.send("💝| https://discord.gg/83Kx5FP5sf")

    
@client.command()
async def server(ctx):
  servers = list(client.guilds)
  for server in servers:
    await ctx.send(server.name)
    

@client.command()
async def deep(ctx):
  servers = list(client.guilds)
  for server in servers:
    await ctx.send(server.name)
    await ctx.send(server.member_count)
    await ctx.send(server.id)
    await ctx.send(server.splash_url)
    await ctx.send("---------------------------------------------------------------")
  


           

    
# keep_alive()
client.run(token)
