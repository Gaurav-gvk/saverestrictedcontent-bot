#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("2856041", default=None, cast=int)
API_HASH = config("05a77e8bcfa4c4d65c4558f22ffe55ff", default=None)
BOT_TOKEN = config("6030116482:AAHjmLKOp-rlSx-JXkiNclVSAucPtNE_j0I", default=None)
SESSION = config("BQCeNkReEwhFNdDPwwIPL2noLNT4GwnMkewTfLWWIR92MAhcAA33YTK8DsaSZYM5SU1fvG5OvbEV1QXEdeT2czyj9FgNpFfvscIM7skFxuoNAxTZdCcHGSQZYvMrhYXphlohMbixC3xvb5w-nqCBy7aR_LxvegrMkkhCBkCyDHJYeUPZVCu5wK7W8IZxLRdRkRvVhHaiSxfoooirIfeN7UEk6ge0acKlnpHlOnGrtdADrz-PW59pFNYRzVG877CRrWR5aiHzMXVbWrPjbVya0jFrwr5TNFZuKqmf8tkj6o1uFTrKQht7ckrpJlVbBpPIl-faIyMH9uyElc-Lh8EivNdBREhyTQA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("Arcturuswithspica", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
