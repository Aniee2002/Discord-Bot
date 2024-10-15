'''
Discord BOT
'''
import discord
import os
import requests
import json
import random

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n       -" + json_data[0]['a']
    return (quote)


if "responding" not in db.keys():
    db["responding"] = True


def new_roasts(roasting_message):
    if "roasts" in db.keys():
        roasts = db["roasts"]
        roasts.append(roasting_message)
        db["roasts"] = roasts
    else:
        db["roasts"] = [roasting_message]


def del_roasts(index):
    roasts = db["roasts"]
    if len(roasts) > index:
        del roasts[index]
        db["roasts"] = roasts


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('&inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('&Inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('&hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('&roast'):
        await message.channel.send(random.choice(db["roasts"]))

    if msg.startswith("&new"):
        roasting_message = msg.split("&new ", 1)[1]
        new_roasts(roasting_message)
        await message.channel.send("New Roast added.")

    if msg.startswith("&del"):
        roasts = []
        if "roasts" in db.keys():
            index = int(msg.split("&del", 1)[1])
            del_roasts(index)
            roasts = db["roasts"]
        await message.channel.send(roasts)
    if msg.startswith("&list"):
        roasts = []
        if "roasts" in db.keys():
            roasts = db["roasts"]
        await message.channel.send(roasts)
    msg_list = msg.split()
    roasting_msg = [
        "Oh {} go buy a brain".format(msg_list[1]),
        "{} is as useless as 'ueue' in 'queue'".format(msg_list[1]),
        "Mirrors can't talk, lucky for {} they can't laugh either".format(msg_list[1]),
        "{} is the reason why God is not talking to us anymore".format(msg_list[1]),
        "I would smack {}, but I'm against animal abuse".format(msg_list[1])
    ]
    if message.content.startswith('!roast'):
        await message.channel.send(random.choice(roasting_msg))


client.run(os.getenv('TOKEN'))
