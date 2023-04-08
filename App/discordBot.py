import logging

import discord
from discord import MessageType
from discord.ext import commands
from controllers import task

proxy_url = 'http://127.0.0.1:7890'
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, proxy=proxy_url)


@bot.event
async def on_ready():
    logging.getLogger(__name__).debug(f"Logged in as mjwrap bot")

@bot.slash_command(description="Make DaVinci say something")
async def hello(ctx, sentence: discord.Option(str)):
    await ctx.respond(sentence)


@bot.slash_command(description="This command is a wrapper of MidJourneyAI")
async def mj_imagine(ctx, prompt: discord.Option(str)):
    logging.getLogger(__name__).debug(prompt)



@bot.slash_command(description="Upscale one of images generated by MidJourney")
async def mj_upscale(ctx, index: discord.Option(int), reset_target: discord.Option(bool) = True):
    logging.getLogger(__name__).debug('mj_upscale')

@bot.slash_command(description="Upscale to max targetted image (should be already upscaled using mj_upscale)")
async def mj_upscale_to_max(ctx):
    logging.getLogger(__name__).debug('mj_upscale_to_max')

@bot.slash_command(description="Make variation given index after target has been set")
async def mj_variation(ctx, index: discord.Option(int), reset_target: discord.Option(bool) = True):
    logging.getLogger(__name__).debug('mj_variation')


@bot.event
async def on_message(message):
    url=None
    for attachment in message.attachments:
        url=attachment.url
        break
    if url:
        for t in task.get_Task_by_prompt(message.content):
            if t.msgType==message.type and t.resultUrl is None:
                task.update_Task(t.id,message.id,url)
                break

bot.run('MTA5MDU3OTg0MTE1MTE0ODA3Mw.GezKQc.nShtw86wyx2RgXVZrW3_ajDkVu5Cjq5xSuqeCc')