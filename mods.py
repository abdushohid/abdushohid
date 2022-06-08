from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌑🌒🌓🌔🌕🌖🌗🌘"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.earth", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)


    

import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.fl(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`chatni buzish boshlanmoqda...`")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   ▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`tayyor!`")


import random
from .. import loader
from asyncio import sleep
class AMod(loader.Module):
	strings = {"name": "LoveMagic"}	
	async def watcher(self, message):
		if message.text != "❤️ magic":
			return
		if message.sender_id == (await message.client.get_me()).id:
			arr = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "💖"]
			h = "🤍"
			first = ""		
			for i in "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4]).split("\n"):
				first += i + "\n"
				await message.edit(first)
				await sleep(0.2)		
			for i in arr:
				await message.edit("".join([h*9, "\n", h*2, i*2, h, i*2, h*2, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h*2, i*5, h*2, "\n", h*3, i*3, h*3, "\n", h*4, i, h*4, "\n", h*9]))
				await sleep(0.3)
			for _ in range(8):
				rand = random.choices(arr, k=34)
				await message.edit("".join([h*9, "\n", h*2, rand[0], rand[1], h, rand[2], rand[3], h*2, "\n", h, rand[4], rand[5], rand[6], rand[7], rand[8],rand[9],rand[10], h, "\n", h, rand[11], rand[12], rand[13], rand[14], rand[15], rand[16],rand[17], h, "\n", h, rand[18], rand[19], rand[20], rand[21], rand[22], rand[23],rand[24], h, "\n", h*2, rand[25], rand[26], rand[27], rand[28], rand[29], h*2, "\n", h*3, rand[30], rand[31], rand[32], h*3, "\n", h*4, rand[33], h*4, "\n", h*9]))
				await sleep(0.3)
			fourth = "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4, "\n", h*9])
			await message.edit(fourth)
			for _ in range(47):
				fourth = fourth.replace("🤍", "❤️", 1)
				await message.edit(fourth)
				await sleep(0.1)
			for i in range(8):
				await message.edit((arr[0]*(8-i)+"\n")*(8-i))
				await sleep(0.4)
			for i in ["I", "I ❤️", "I ❤️ U", "I ❤️ U!"]:
				await message.edit(f"<b>{i}</b>")
				await sleep(0.5)


from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Police"}
	@loader.owner
	async def policecmd(self, message):
		for _ in range(12):
			for police in ['🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵','🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴']:
				await message.edit(police)
				await sleep(0.3)



from .. import loader 
from asyncio import sleep  
 
def register(cb): 
 cb(SnowMod())  
  
class SnowMod(loader.Module): 
 """Снег""" 
 strings = {'name': 'Снег'} 
         
 async def snowcmd(self, message): 
  """Используй .snow""" 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit(' ☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n   ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')  
  await sleep(1.25) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️  \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
  await sleep(0.75) 
  await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')



version = (12, 3, 7)

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 

@loader.tds
class SpotifyDownloaderMod(loader.Module):
    """Music search module"""
    strings = {
        "name": "MusicFinder",
        "yoq": "<b>♫︎ Nothing found!</b>",
        "qidiryapman": "<b>🧐 Qdirvoma...</b>",
        "eshe": "<b>♫︎ Keyinro urinib kor!</b>",
        "topmadim": "<b>♫︎ Tori yoz . Bilib yozmasen qiyin?</b>"}
    
    async def client_ready(self, client, db):
        self.client = client
        self._db = db
        self._me = await client.get_me()
        
    @loader.unrestricted
    async def vkcmd(self, message):
        """qowu ismi"""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit(self.strings("yoq", message))

        message = await message.edit(self.strings("qidiryapman", message))
        try:
            message = message[0]
        except: pass
        music = await self.client.inline_query('spotifysavebot', args)
        for mus in music:
            if mus.result.type == 'audio':
                await self.client.send_file(message.peer_id, mus.result.document, reply_to=message.reply_to_msg_id, caption="♫︎ <b>Qowu topildi!\n♫︎ 🇺🇿Egasi🇺🇿</b> <code>@WhiteWolf_NinjaLive UzbekSila</code>")
                return await message.delete()

        return await message.edit(self.strings("topmadim", message))

    async def spotycmd(self, message): 
        """qoshu yo albom ismi""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit(self.strings("yoq", message))
        try: 
            await message.edit(self.strings("qidiryapman", message))
            music = await message.client.inline_query('lybot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, caption="♫︎ <b>Qoshu topildi naxoy!\n♫︎️ 🇺🇿Egasi🇺🇿 by</b> <code>@WhiteWolf_NinjaLive</code>", reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"♫︎ <b>{args}</b> - Qowu topilmad!\n♫︎ <b> Yoki manbindan qdrip kor <code> .vk</code>?</b>")
