import asyncio
import datetime
import time

from . import *

ping_txt = """<b><i>╰PONG╯</b></i>

    ⚘  <i>ʂ℘ɛɛɖ :</i> <code>{}</code>
    ⚘  <i>ų℘ɬıɱɛ :</i> <code>{}</code>
    ⚘  <i>ơῳŋɛཞ :</i> {}"""


@userbot_cmd(pattern="ping$")
async def pong(userbot):
    start = datetime.datetime.now()
    event = await eor(userbot, "`·.·★ PING ★·.·´")
    cid = await client_id(event)
    ForGo10God, USERBOT_USER = cid[0], cid[1]
    userbot_mention = f"<a href='tg://user?id={ForGo10God}'>{USERBOT_USER}</a>"
    uptime = await get_time((time.time() - StartTime))
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(ping_txt.format(ms, uptime, userbot_mention), parse_mode="HTML")


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your EAGLE MAFIA OP BOT"
).add_warning(
  "✅ Harmless Module"
).add()
