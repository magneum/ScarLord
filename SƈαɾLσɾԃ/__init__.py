from Deve import *
from Storeroom import *
from logging import INFO, basicConfig, getLogger
StartTime = time.time()
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGGER = getLogger(__name__)

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