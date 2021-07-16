from Deve import *
from Booger import *
from Storeroom import *

StartTime = time.time()
LOGGER = POG

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("SƈαɾLσɾԃ", API_ID, API_HASH)
dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
from Bytes.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler