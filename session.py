from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 33505232
api_hash = "36d92982097114a1a98c0b82b35ec015"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())