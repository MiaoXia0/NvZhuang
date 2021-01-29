from nonebot import MessageSegment
from hoshino import Service
from hoshino.typing import CQEvent, HoshinoBot
from .config import *

sv = Service('NvZhuang', enable_on_default=False)
qq = QQ
at = AT


@sv.on_fullmatch('at被迫害者')
async def setAt(bot, ev):
    global at
    at = True
    await bot.send(ev, '已设置@被迫害者')


@sv.on_fullmatch('不at被迫害者')
async def setnoAt(bot, ev):
    global at
    at = False
    await bot.send(ev, '已设置不@被迫害者')


@sv.on_prefix('设置迫害QQ')
async def SetNvZhuangQQ(bot, ev):
    global qq
    qq = int(ev.message.extract_plain_text())
    await bot.send(ev, '已将被迫害者QQ设为' + str(qq))


@sv.on_fullmatch('女装迫害')
async def XuYuNvZhuang(bot: HoshinoBot, ev: CQEvent):
    if at:
        await bot.send(ev, MessageSegment.at(qq) + '女装！')
    else:
        nickname = bot.get_stranger_info(user_id=qq, no_cache=True)['nickname']
        await bot.send(ev, nickname + '女装！')
