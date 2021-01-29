from nonebot import MessageSegment
from hoshino import Service
from hoshino.typing import CQEvent, HoshinoBot
from .config import *
try:
    import ujson as json
except ImportError:
    import json

sv = Service('NvZhuang', enable_on_default=False)
# qq = QQ
# at = AT
config = json.load(open('config.json', 'r'))

@sv.on_fullmatch('at被迫害者')
async def setAt(bot: HoshinoBot, ev: CQEvent):
    # global at
    # at = True
    groupid = await ev.group_id
    groupid = str(groupid)
    config[groupid]['AT'] = True
    json.dump(config, open('config.json', 'w'))
    await bot.send(ev, '已设置@被迫害者')



@sv.on_fullmatch('不at被迫害者')
async def setnoAt(bot: HoshinoBot, ev: CQEvent):
    # global at
    # at = False
    groupid = await ev.group_id
    groupid = str(groupid)
    config[groupid]['AT'] = False
    json.dump(config, open('config.json', 'w'))
    await bot.send(ev, '已设置不@被迫害者')


@sv.on_prefix('设置迫害QQ')
async def SetNvZhuangQQ(bot: HoshinoBot, ev: CQEvent):
    # global qq
    # config
    # qq = int(ev.message.extract_plain_text())
    groupid = await ev.group_id
    groupid = str(groupid)
    config[groupid]['QQ'] = int(ev.message.extract_plain_text())
    json.dump(config, open('config.json', 'w'))
    await bot.send(ev, '已将被迫害者QQ设为' + str(config[groupid]['QQ']))


@sv.on_fullmatch('女装迫害')
async def NvZhuang(bot: HoshinoBot, ev: CQEvent):
    groupid = await ev.group_id
    groupid = str(groupid)
    if config[groupid]['AT']:
        await bot.send(ev, MessageSegment.at(config[groupid]['QQ']) + '女装！')
    else:
        info = await bot.get_stranger_info(user_id=config[groupid]['QQ'], no_cache=True)
        nickname = info['nickname']
        await bot.send(ev, nickname + '女装！')
