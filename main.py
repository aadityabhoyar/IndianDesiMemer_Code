import os
import discord
from discord.ext import commands
import numpy as np
import random
from random import random
import requests


token = ("OTg3MzkxODM2ODg2Nzk0MjYw.GdcrEZ.9doj-vNH-_dwfRBsKxFFlr2HBkEfWFULgaDQVU")

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
        "https://discord.com/api/oauth2/authorize?client_id=986632998503997500&permissions=122406824960&scope=bot",
        color=0xF49726)
    embed.add_field(
        name="Command Categories :",
        value="🐸 `memes    :` Image generation with a memey twist.\n" +
        "🌝 `fun      :` Entertainment! **Bus Thoda Sambhal Ke**\n" +
        "🎲 `random   :` Just some random stuff\n" +
        "👻 `fantasy  :` Fantasy Entertainment ! **Bus Thoda Sambhal Ke**\n" +
        "🤗 `emotions :` Share Your Emotion\n" +
        "🔧 `utility  :` Bot utility zone\n\n" +
        "To view the commands of a category, send `yar help <category>`\n\n[Add the Bot](https://discord.com/api/oauth2/authorize?client_id=986632998503997500&permissions=122406824960&scope=bot) - [Need Support?](https://discord.com/api/oauth2/authorize?client_id=986632998503997500&permissions=122406824960&scope=bot) - [Join the Community](https://discord.com/api/oauth2/authorize?client_id=986632998503997500&permissions=122406824960&scope=bot)",
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
        "Commands of **meme** \n`yar meme     :` Complet Dsei Memes\n`yar engmeme  :` English memes\n`yar dank     :` Desi Dank Memes\n`yar engdank  :` English Dank Memes\n`yar animeme  :` Anime Memes\n`yar nsmeme   :` NSFW  memes\n`yar bakchodi :` Backchodi",
        color=0xF49726)
    embed.add_field(name="\nThere r many memes which can trigged you 😬",
                    value="`So ,Sorry in Advance`",
                    inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


# @help.command ()
# async def games(ctx) :
#     embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **games** \n`yar 8ball :` Get Answer In Ha ya Naa\n`yar roll  :` Roll The Dice", color=0xF49726)
#     embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
#     await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **fun** \nIt contain NSFW content,**Tu Thoda Sambhal Ke** **NSFW**\n||`yar tites       :` Randome Tites Images\n`yar desitites   :` Only Desi Tits\n`yar blowjob     :` Blowjob\n`yar randomnsfw  :` Random NSFW Content||",
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


@help.command()
async def fantasy(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **fantasy** \nIt contain NSFW content,**Tu Thoda Sambhal Ke** **NSFW**\n||`yar wsifu       :` Wsifu \n`yar neko        :` Neko\n`yar teap        :` Something\n`yar aniblowjob  :`Anime Blowjob||",
        color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@help.command()
async def emotions(ctx):
    embed = discord.Embed(
        title="IndianDesiMemer Help Center ✨",
        description=
        "Commands of **emotions** \n`yar blush       :`\n`yar cry         :`\n`yar sleepy      :`\n`yar smile       :`\n`yar thumbsup    :`\n`yar wave         :`\n`yar thinking    :`\n`yar triggered   :`\n`yar happy       :`",
        color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@help.command()
async def utility(ctx):
    embed = discord.Embed(title="IndianDesiMemer Help Center ✨",
                          description="Commands of **utility** \n ",
                          color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Command requested by: {}".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


##############################################################


@client.command()
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
async def engmeme(ctx):
    response = requests.get("https://meme-api.herokuapp.com/gimme/" + "memes" +
                            "NSFW_IndianMemes" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍\t " + uv + "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
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
    embed.set_footer(text="\n👍\t  " + uv + "By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
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
    embed.set_footer(text="\n👍\t  " + uv + "By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
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
    embed.set_footer(text="\n👍\t  " + uv + "By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
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
    embed.set_footer(text="\n👍\t  " + uv + "By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
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
    embed.set_footer(text="\n👍\t  " + uv + "By :r/" + subreddit)
    await ctx.send(embed=embed)


##########################################################################################################


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            "**Ruko Zara Sabar Karo**\n ⚠ `{0} second` baad try karna ⚠".
            format(round(error.retry_after, 2)))

    # await ctx.send("\n ⚠ {0} second baad try karna ⚠".format(round(error.retry_after, 2)))


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def tites(ctx):
    memeLink = ["tits", "BreedingMaterial", "hugeboobs", "BigBoobsGW"]
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
    embed.set_footer(
        icon_url=ctx.author.avatar_url,
        text="Requested by: {}  😏 ".format(ctx.author.display_name) +
        "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def desitites(ctx):
    # memeLink = ["desimemes","subtleindiantraits","DesiAdultMemesCaption","DankIndianMeme"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            "indianboobs" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(
        icon_url=ctx.author.avatar_url,
        text="Requested by: {}  😏".format(ctx.author.display_name) +
        "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def blowjob(ctx):
    # memeLink = ["desimemes","subtleindiantraits","DesiAdultMemesCaption","DankIndianMeme"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            "BlowJob" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(
        icon_url=ctx.author.avatar_url,
        text="Requested by: {}  😏".format(ctx.author.display_name) +
        "  By :r/" + subreddit)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def randomnsfw(ctx):
    # memeLink = ["desimemes","subtleindiantraits","DesiAdultMemesCaption","DankIndianMeme"]
    response = requests.get("https://meme-api.herokuapp.com/gimme/" +
                            "BreedingMaterial" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)
    subreddit = (m["subreddit"])
    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(
        icon_url=ctx.author.avatar_url,
        text="Requested by: {}  😏".format(ctx.author.display_name) +
        "  By :r/" + subreddit)
    await ctx.send(embed=embed)


###########################################################################################################


@client.command()
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
                     text="\n👍\t" + uv +
                     "  Requested by: {}  😏".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
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
                     text="\n👍\t" + uv +
                     "  Requested by: {}  ".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
async def foodporn(ctx):
    response = requests.get(
        "https://meme-api.herokuapp.com/gimme/IndianFoodPhotos" + "?t=all?hot")
    m = response.json()
    postLink = (m["postLink"])
    title = (m["title"])
    imageUrl = (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed = discord.Embed(title=title, url=postLink, color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="\n👍\t" + uv +
                     "  Requested by: {}  ".format(ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
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
                     text="  Requested by: {}  ".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


# @client.command()
# async def aniquote(ctx):
#     response = requests.get("https://animechan.vercel.app/api/random")
#     m = response.json()
#     anime = (m["anime"])
#     character = (m["character"])
#     quote =  (m["url"])

#     embed=discord.Embed(title= anime + quote,color=0xF49726)

#     embed.set_footer(icon_url=ctx.author.avatar_url,text="  Requested by: {}  ".format(ctx.author.display_name))
#     await ctx.send(embed=embed)
#


@client.command()
async def hi(ctx):

    await ctx.send("aur {0} kaise".format(ctx.message.author.name))
    await ctx.send(
        "https://cdn.discordapp.com/emojis/984161048863064136.gif?size=60&quality=lossless&size=40"
    )


@client.command()
async def hello(ctx):

    await ctx.send("aur {0} kaise".format(ctx.message.author.name))
    await ctx.send(
        "https://cdn.discordapp.com/emojis/984161048863064136.gif?size=60&quality=lossless&size=40"
    )


###########################################################################################################


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def wsifu(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/waifu")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Requested by: {}  😏".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def neko(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/neko")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Requested by: {}  😏".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def teap(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/teap")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Requested by: {}  😏".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 25, commands.BucketType.channel)
async def aniblowjob(ctx):
    response = requests.get("https://api.waifu.pics/nsfw/blowjob")
    q = response.json()
    image = (q['url'])
    embed = discord.Embed(color=0xFF5733)
    embed.set_image(url=image)
    embed.set_footer(icon_url=ctx.author.avatar_url,
                     text="Requested by: {}  😏".format(
                         ctx.author.display_name))
    await ctx.send(embed=embed)


#############################################################################################################


@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
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


############################################################################################################
@client.command()
async def ping(ctx):
    await ctx.send('Ping! **{0}**ms'.format(round(client.latency * 1000)))
    await ctx.send(
        "Socha nahi tha koi yeh **command** use karega \n {0} Q".format(
            ctx.message.author.name))

    await ctx.send(
        "https://cdn.discordapp.com/emojis/986684266257743913.webp?size=60&quality=lossless&size=40"
    )



client.run(token)
