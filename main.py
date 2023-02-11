import os
import random
import re
import datetime
import json
import time
import logging
from datetime import datetime, timedelta
from khl import *
from khl.command import *
from khl.card import *
from keep_alive import keep_alive

bot = Bot(os.getenv("bot_token"))

@bot.command(name='test')
async def world(msg: Message):
    await msg.reply('Hello World!')
  
@bot.command()
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'你得到了 {result}')

@bot.command()
async def Help(msg: Message):
    logging(msg)
    cm = CardMessage()
    c3 = Card(Module.Header('目前支持的指令如下！'))
    c3.append(Module.Divider())
    c3.append(Module.Section(Element.Text('??', Types.Text.KMD)))
    c3.append(Module.Divider())
    c3.append(
        Module.Section(
            '有任何问题，请加入帮助服务器与我联系',
            Element.Button('帮助', 'https://kook.top/XX', Types.Click.LINK)))
    cm.append(c3)
    await msg.reply(cm)


# 测试
@bot.command()
async def card(msg: Message):
    c = Card(Module.Header('CardMessage'), Module.Section('test'))
    cm = CardMessage(
        c)  
    await msg.reply(cm)


# 倒计时
@bot.command()
async def countdown(msg: Message):
    cm = CardMessage()

    c1 = Card(Module.Header('倒计时1小时'),
              color='#5A3BD7')  
    c1.append(Module.Divider())
    c1.append(
        Module.Countdown(datetime.now() + timedelta(hours=1),
                         mode=Types.CountdownMode.SECOND))
    cm.append(c1)

    await msg.reply(cm)

def logging(msg: Message):
    now_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
    print(
        f"[{now_time}] G:{msg.ctx.guild.id} - C:{msg.ctx.channel.id} - Au:{msg.author_id}_{msg.author.username}#{msg.author.identify_num} - content:{msg.content}"
    )


def logging2(e: Event):
    now_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{now_time}] Event:{e.body}")


keep_alive()
bot.run()
