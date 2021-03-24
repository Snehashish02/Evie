from sys import argv, exit
from Miley import tbot
from Miley import TOKEN

import Miley.events

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

if len(argv) not in (1, 3, 4):
    tbot.disconnect()
else:
    tbot.run_until_disconnected()