from nonebot import MessageSegment
from hoshino import Service
from .config import *

sv = Service('NvZhuang', enable_on_default=False)


@sv.on_keyword('女装')
async def XuYuNvZhuang(bot, ev):
    if AT:
        await bot.send(ev, MessageSegment.at(1272483979) + '须臾女装！')
    else:
        await bot.send(ev, '须臾女装！')
