from random import random

from nonebot import MessageSegment
from hoshino import Service, R
from hoshino.typing import CQEvent, HoshinoBot
import os

try:
    import ujson as json
except ImportError:
    import json

sv = Service('NvZhuang')
try:
    config = json.load(open(os.path.dirname(__file__) + '/config.json', 'r'))
except IOError:
    config = {}
    json.dump(config, open(os.path.dirname(__file__) + '/config.json', 'w'))


@sv.on_fullmatch('at被迫害者')
async def setAt(bot: HoshinoBot, ev: CQEvent):
    groupid = ev.group_id
    groupid = str(groupid)
    try:
        qq = config[groupid]['QQ']
    except KeyError:
        await bot.send(ev, '请先设置迫害者QQ')
        return
    config[groupid] = {'AT': True, 'QQ': qq}
    json.dump(config, open(os.path.dirname(__file__) + '/config.json', 'w'))
    await bot.send(ev, '已设置@被迫害者')


@sv.on_fullmatch('不at被迫害者')
async def setnoAt(bot: HoshinoBot, ev: CQEvent):
    groupid = ev.group_id
    groupid = str(groupid)
    try:
        qq = config[groupid]['QQ']
    except KeyError:
        await bot.send(ev, '请先设置迫害者QQ')
        return
    config[groupid] = {'AT': False, 'QQ': qq}
    json.dump(config, open(os.path.dirname(__file__) + '/config.json', 'w'))
    await bot.send(ev, '已设置不@被迫害者')


@sv.on_prefix('设置迫害QQ')
async def SetNvZhuangQQ(bot: HoshinoBot, ev: CQEvent):
    groupid = ev.group_id
    groupid = str(groupid)
    try:
        at = config[groupid]['AT']
    except KeyError:
        at = False
    config[groupid] = {'AT': at, 'QQ': int(ev.message.extract_plain_text())}
    json.dump(config, open(os.path.dirname(__file__) + '/config.json', 'w'))
    await bot.send(ev, '已将被迫害者QQ设为' + str(config[groupid]['QQ']))


@sv.on_fullmatch('女装迫害')
async def NvZhuang(bot: HoshinoBot, ev: CQEvent):
    groupid = ev.group_id
    groupid = str(groupid)
    imgs = os.listdir(R.img('NvZhuang/').path)
    img=R.img('NvZhuang/' + random.choice(imgs))
    try:
        if config[groupid]['AT']:
            await bot.send(ev, MessageSegment.at(config[groupid]['QQ']) + '女装！\n' + img.cqcode)
        else:
            info = await bot.get_stranger_info(user_id=config[groupid]['QQ'], no_cache=True)
            nickname = info['nickname']
            await bot.send(ev, nickname + '女装！\n' + img.cqcode)
    except KeyError:
        await bot.send(ev, '请先设置迫害QQ')
