import asyncio
from telethon import TelegramClient
from datetime import datetime

api_id = 25922736
api_hash = 'fbcd477c822490edbb89d2a6ee4d6707'
phone_number = '+94779451939'
target_groups = ["yotube0","LinkShare_Earn","earning_group_1","Links_OnlyX","leeklanthee","sharelinkairdroup"]

message_to_send = " 🎬😀 World of Sex💋 💫

😈  ✅✅✅✅✅  😈

🐚🐚🐚🐚🐚🐚🐚🐚🐚🐚

⚡️Leaked Video
➜ https://t.me/allvideo_18

⚡️Leaked Photo
➜ https://t.me/allvideo_18

⚡️Couple Video
➜ https://t.me/allvideo_18

⚡️Blowjob Video
➜ https://t.me/allvideo_18

⚡️The Piece That Got Fucked in the Room
➜ https://t.me/allvideo_18

⚡️Girl Bath Eve
➜ https://t.me/allvideo_18

⚡️Antilles Video
➜ https://t.me/allvideo_18

⚡️Secretly Seduced
➜https://t.me/allvideo_18
Everyone be 😚😌😚😋

🔗🔤🔤🥵🥵
https://t.me/allvideo_18
"

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    while True:
        for group in target_groups:
            try:
                await client.send_message(group, message_to_send)
                print(f"[{datetime.now()}] Sent to {group}")
            except Exception as e:
                print(f"Error sending to {group}: {e}")
        await asyncio.sleep(1800)  # Send every hour

with client:
    client.loop.run_until_complete(main())
