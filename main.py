import json
import discord

bot = discord.Client()

f = open('config.json')
config = json.load(f)
keywords = config['keywords']
send_channel = int(config['send_channel'])

@bot.event
async def on_ready():
    print(f"{bot.user} has connected.")

@bot.event
async def on_message(message):
    a=bool(config['ping_OnAlert'])
    if a: a = "@everyone"
    else: a = ""
    c = bot.get_channel(send_channel)
    if message.author.id == 570700068198547466:
        embeds = message.embeds # return list of embeds
        if embeds:
            for embed in embeds:
                try:
                    if keywords[0] in embed.footer.text:
                        await c.send(f"Wishlisted servent spawn in {message.jump_url} {embed.image.url} {a}")
                        print("Wishlisted Servent message sent")
                    elif keywords[1] in embed.footer.text:
                        await c.send(f"Server spawn in {message.jump_url} {embed.image.url} {a}")
                        print("Server spawn message sent")
                except TypeError:
                    return

bot.run(config['token'])
