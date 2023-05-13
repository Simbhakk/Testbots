#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button
from .database import Database
from pyrogram.types import Message
from .. import AUTH

from main.plugins.database import add_user, del_user, full_userbase, present_user


from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/broadcast'))

async def send_text(client: Bot, message: Message):

    if message.reply_to_message:

        query = await full_userbase()

        broadcast_msg = message.reply_to_message

        total = 0

        successful = 0

        blocked = 0

        deleted = 0

        unsuccessful = 0

        

        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")

        for chat_id in query:

            try:

                await broadcast_msg.copy(chat_id)

                successful += 1

            except FloodWait as e:

                await asyncio.sleep(e.x)

                await broadcast_msg.copy(chat_id)

                successful += 1

            except UserIsBlocked:

                await del_user(chat_id)

                blocked += 1

            except InputUserDeactivated:

                await del_user(chat_id)

                deleted += 1

            except:

                unsuccessful += 1

                pass

            total += 1

        

        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>

Successful: <code>{successful}</code>

Blocked Users: <code>{blocked}</code>

Deleted Accounts: <code>{deleted}</code>

Unsuccessful: <code>{unsuccessful}</code></b>"""

        

        return await pls_wait.edit(status)

    else:

        msg = await message.reply(REPLY_ERROR)

        await asyncio.sleep(8)

        await msg.delete()

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Send me Link of any message to clone it here, For private channel message, send invite link first"
    await start_srb(event, text)
    
