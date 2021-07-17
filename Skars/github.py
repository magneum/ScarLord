# import Database.github_sql as sql
# from Database.clear_cmd_sql import get_clearcmd
# from SƈαɾLσɾԃ import dispatcher
# from Bytes.chat_status import user_admin
# from Bytes.misc import delete
# from Skars.disable import DisableAbleCommandHandler
# import Bytes.git_api as api


# def getphh(index):
#     recentRelease = api.getReleaseData(api.getData("phhusson/treble_experimentations"), index)
#     if recentRelease is None:
#         return "The specified release could not be found"
#     author = api.getAuthor(recentRelease)
#     authorUrl = api.getAuthorUrl(recentRelease)
#     name = api.getReleaseName(recentRelease)
#     assets = api.getAssets(recentRelease)
#     releaseName = api.getReleaseName(recentRelease)
#     message = "<b>Author:</b> <a href='{}'>{}</a>\n".format(authorUrl, author)
#     message += "<b>Release Name:</b> <code>"+releaseName+"</code>\n\n"
#     message += "<b>Assets:</b>\n"
#     for asset in assets:
#         fileName = api.getReleaseFileName(asset)
#         if fileName in ("manifest.xml", "patches.zip"):
#             continue
#         fileURL = api.getReleaseFileURL(asset)
#         assetFile = "• <a href='{}'>{}</a>".format(fileURL, fileName)
#         sizeB = ((api.getSize(asset))/1024)/1024
#         size = "{0:.2f}".format(sizeB)
#         message += assetFile + "\n"
#         message += "    <code>Size: "  + size + " MB</code>\n"
#     return message


# # do not async
# def getData(url, index):
#     if not api.getData(url):
#         return "Invalid <user>/<repo> combo"
#     recentRelease = api.getReleaseData(api.getData(url), index)
#     if recentRelease is None:
#         return "The specified release could not be found"
#     author = api.getAuthor(recentRelease)
#     authorUrl = api.getAuthorUrl(recentRelease)
#     name = api.getReleaseName(recentRelease)
#     assets = api.getAssets(recentRelease)
#     releaseName = api.getReleaseName(recentRelease)
#     message = "*Author:* [{}]({})\n".format(author, authorUrl)
#     message += "*Release Name:* " + releaseName + "\n\n"
#     for asset in assets:
#         message += "*Asset:* \n"
#         fileName = api.getReleaseFileName(asset)
#         fileURL = api.getReleaseFileURL(asset)
#         assetFile = "[{}]({})".format(fileName, fileURL)
#         sizeB = ((api.getSize(asset)) / 1024) / 1024
#         size = "{0:.2f}".format(sizeB)
#         downloadCount = api.getDownloadCount(asset)
#         message += assetFile + "\n"
#         message += "Size: " + size + " MB"
#         message += "\nDownload Count: " + str(downloadCount) + "\n\n"
#     return message


# # likewise, aux function, not async
# def getRepo(bot, update, reponame):
#     chat_id = update.effective_chat.id
#     repo = sql.get_repo(str(chat_id), reponame)
#     if repo:
#         return repo.value, repo.backoffset
#     return None, None


# def getRelease(update: Update, context: CallbackContext):
#     bot, args = context.bot, context.args
#     msg = update.effective_message
#     if len(args) == 0:
#         msg.reply_text("Please use some arguments!")
#         return
#     if (
#         len(args) != 1
#         and not (len(args) == 2 and args[1].isdigit())
#         and not ("/" in args[0])
#     ):
#         deletion(update, context, msg.reply_text("Please specify a valid combination of <user>/<repo>"))
#         return
#     index = 0
#     if len(args) == 2:
#         index = int(args[1])
#     url = args[0]
#     text = getData(url, index)
#     deletion(update, context, msg.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True))
#     return


# def hashFetch(update: Update, context: CallbackContext):  # kanged from notes
#     bot, args = context.bot, context.args
#     message = update.effective_message.text
#     msg = update.effective_message
#     fst_word = message.split()[0]
#     no_hash = fst_word[1:]
#     url, index = getRepo(bot, update, no_hash)
#     if url is None and index is None:
#         deletion(update, context, msg.reply_text(
#             "There was a problem parsing your request. Likely this is not a saved repo shortcut",
#             parse_mode=ParseMode.MARKDOWN,
#             disable_web_page_preview=True,
#         ))
#         return
#     text = getData(url, index)
#     deletion(update, context, msg.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True))
#     return


# def cmdFetch(update: Update, context: CallbackContext):
#     bot, args = context.bot, context.args
#     msg = update.effective_message
#     if len(args) != 1:
#         deletion(update, context, msg.reply_text("Invalid repo name"))
#         return
#     url, index = getRepo(bot, update, args[0])
#     if url is None and index is None:
#         deletion(update, context, msg.reply_text(
#             "There was a problem parsing your request. Likely this is not a saved repo shortcut",
#             parse_mode=ParseMode.MARKDOWN,
#             disable_web_page_preview=True,
#         ))
#         return
#     text = getData(url, index)
#     deletion(update, context, msg.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True))
#     return


# def changelog(update: Update, context: CallbackContext):
#     bot, args = context.bot, context.args
#     msg = update.effective_message
#     if len(args) != 1:
#         deletion(update, context, msg.reply_text("Invalid repo name"))
#         return
#     url, index = getRepo(bot, update, args[0])
#     if not api.getData(url):
#         msg.reply_text("Invalid <user>/<repo> combo")
#         return
#     data = api.getData(url)
#     release = api.getReleaseData(data, index)
#     body = api.getBody(release)
#     deletion(update, context, msg.reply_text(body))
#     return


# @user_admin
# def saveRepo(update: Update, context: CallbackContext):
#     bot, args = context.bot, context.args
#     chat_id = update.effective_chat.id
#     msg = update.effective_message
#     if (
#         len(args) != 2
#         and (len(args) != 3 and not args[2].isdigit())
#         or not ("/" in args[1])
#     ):
#         deletion(update, context, msg.reply_text("Invalid data, use <reponame> <user>/<repo> <value (optional)>"))
#         return
#     index = 0
#     if len(args) == 3:
#         index = int(args[2])
#     sql.add_repo_to_db(str(chat_id), args[0], args[1], index)
#     deletion(update, context, msg.reply_text("Repo shortcut saved successfully!"))
#     return


# @user_admin
# def delRepo(update: Update, context: CallbackContext):
#     bot, args = context.bot, context.args
#     chat_id = update.effective_chat.id
#     msg = update.effective_message
#     if len(args) != 1:
#         msg.reply_text("Invalid repo name!")
#         return
#     sql.rm_repo(str(chat_id), args[0])
#     deletion(update, context, msg.reply_text("Repo shortcut deleted successfully!"))
#     return


# def listRepo(update: Update, context: CallbackContext):
#     chat_id = update.effective_chat.id
#     chat = update.effective_chat
#     chat_name = chat.title or chat.first or chat.username
#     repo_list = sql.get_all_repos(str(chat_id))
#     msg = "*List of repo shotcuts in {}:*\n"
#     des = "You can get repo shortcuts by using `/fetch repo`, or `&repo`.\n"
#     for repo in repo_list:
#         repo_name = " • `{}`\n".format(repo.name)
#         if len(msg) + len(repo_name) > MAX_MESSAGE_LENGTH:
#             deletion(update, context, update.effective_message.reply_text(msg, parse_mode=ParseMode.MARKDOWN))
#             msg = ""
#         msg += repo_name
#     if msg == "*List of repo shotcuts in {}:*\n":
#         deletion(update, context, update.effective_message.reply_text("No repo shortcuts in this chat!"))
#     elif len(msg) != 0:
#         deletion(update, context, update.effective_message.reply_text(
#             msg.format(chat_name) + des, parse_mode=ParseMode.MARKDOWN
#         ))


# def getVer(update: Update, context: CallbackContext):
#     msg = update.effective_message
#     ver = api.vercheck()
#     deletion(update, context, msg.reply_text("GitHub API version: " + ver))
#     return


# def deletion(update: Update, context: CallbackContext, delmsg):
#     chat = update.effective_chat
#     cleartime = get_clearcmd(chat.id, "github")

#     if cleartime:
#         context.dispatcher.run_async(delete, delmsg, cleartime.time)


# __help__ = """
# *Github module. This module will fetch github releases*\n
# *Available commands:*
#  • `/git <user>/<repo>`: will fetch the most recent release from that repo.
#  • `/git <user>/<repo> <number>`: will fetch releases in past.
#  • `/fetch <reponame> or &reponame`: same as `/git`, but you can use a saved repo shortcut
#  • `/listrepo`: lists all repo shortcuts in chat
#  • `/gitver`: returns the current API version
#  • `/changelog <reponame>`: gets the changelog of a saved repo shortcut
 
# *Admin only:*
#  • `/saverepo <name> <user>/<repo> <number (optional)>`: saves a repo value as shortcut
#  • `/delrepo <name>`: deletes a repo shortcut
# """

# __Hype_Scar_Var__ = "GitHub"


# RELEASE_HANDLER = DisableAbleCommandHandler(
#     "git", getRelease, admin_ok=True, run_async=True
# )
# FETCH_HANDLER = DisableAbleCommandHandler(
#     "fetch", cmdFetch, admin_ok=True, run_async=True
# )
# SAVEREPO_HANDLER = CommandHandler("saverepo", saveRepo, run_async=True)
# DELREPO_HANDLER = CommandHandler("delrepo", delRepo, run_async=True)
# LISTREPO_HANDLER = DisableAbleCommandHandler("listrepo", listRepo, admin_ok=True, run_async=True)
# VERCHECKER_HANDLER = DisableAbleCommandHandler("gitver", getVer, admin_ok=True, run_async=True)
# CHANGELOG_HANDLER = DisableAbleCommandHandler(
#     "changelog", changelog, admin_ok=True, run_async=True
# )

# HASHFETCH_HANDLER = RegexHandler(r"^&[^\s]+", hashFetch)

# dispatcher.add_handler(RELEASE_HANDLER)
# dispatcher.add_handler(FETCH_HANDLER)
# dispatcher.add_handler(SAVEREPO_HANDLER)
# dispatcher.add_handler(DELREPO_HANDLER)
# dispatcher.add_handler(LISTREPO_HANDLER)
# dispatcher.add_handler(HASHFETCH_HANDLER)
# dispatcher.add_handler(VERCHECKER_HANDLER)
# dispatcher.add_handler(CHANGELOG_HANDLER)
# 



#"|============================================================|🚀|============================================================|"
# from telegram.error import BadRequest
# from functools import wraps
# import importlib
# import html
# import subprocess
# from datetime import datetime
# from bs4 import BeautifulSoup
# from requests import get
# from telegram import Bot, Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, MessageHandler
# from telegram.ext import CallbackContext, run_async
# from ujson import loads
# from yaml import load, Loader
# from typing import Optional, List
# import re
# from telegram.error import BadRequest
# from telegram.ext import (
#     CallbackContext,
#     CallbackQueryHandler,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# from telegram import Message, Chat, Update, User, ChatPermissions
# from telegram.utils.helpers import mention_html, escape_markdown
# import json, time, os
# from io import BytesIO
# from telegram.ext import CallbackContext, run_async, CallbackQueryHandler
# import html
# from telegram import ParseMode, Message, Update
# from telegram.error import BadRequest
# from telegram.ext import CommandHandler, CallbackContext, run_async
# from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
# from telegram.utils.helpers import mention_html
# from telegram.error import BadRequest
# import importlib
# import html
# from telegram import ParseMode, Update
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
# from telegram.utils.helpers import mention_html
# import os
# import html
# import html
# from typing import Optional
# from telegram import Chat, Message, ParseMode, Update, User, ChatPermissions
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler
# from telegram.ext.dispatcher import run_async
# from telegram.utils.helpers import mention_html, mention_markdown
# import re
# from telegram import ParseMode, ChatPermissions, Update
# from telegram.error import BadRequest
# from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, run_async
# from telegram.utils.helpers import mention_html

# from telegram import ParseMode, Update
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# import html
# from telegram import ParseMode, Update
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, CommandHandler, run_async
# from telegram.utils.helpers import mention_html
# from telegram import Update, Bot, ParseMode
# from telegram.ext import CommandHandler, CallbackContext, run_async
# from telegram import Update, ParseMode
# from telegram.ext import CallbackContext, CommandHandler, run_async
# import time
# import re
# from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
# from telegram.error import BadRequest, Unauthorized
# from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, run_async
# import requests
# import subprocess
# import sys
# import re
# import random
# from html import escape
# import telegram
# from telegram import ParseMode, InlineKeyboardMarkup, Message, InlineKeyboardButton, Update
# from telegram.error import BadRequest
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     MessageHandler,
#     DispatcherHandlerStop,
#     CallbackQueryHandler,
#     run_async,
#     Filters,
# )
# from telegram.utils.helpers import mention_html, escape_markdown
# from contextlib import suppress
# from time import sleep
# from telegram import TelegramError, Update
# from telegram.error import Unauthorized
# from telegram.ext import CallbackContext, CommandHandler, run_async
# from typing import Union
# from telegram import ParseMode, Update
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     RegexHandler,
# )
# from future.utils import string_types
# from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import CallbackContext, CommandHandler
# import html
# import traceback
# import requests
# from telegram.utils.helpers import escape_markdown
# import html
# import random
# import traceback
# import sys
# import pretty_errors
# import io
# import ast
# import csv
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, CommandHandler, run_async
# import io
# import os
# import textwrap
# import traceback
# from telegram import (
#     InlineKeyboardButton,
#     InlineKeyboardMarkup,
#     MessageEntity,
#     ParseMode,
#     Update,
# )
# from telegram.error import BadRequest, TelegramError, Unauthorized
# from telegram.ext import (
#     CallbackContext,
#     CallbackQueryHandler,
#     CommandHandler,
#     run_async,
# )
# from telegram.utils.helpers import mention_html, mention_markdown
# import json
# import os
# import re
# import time
# import uuid
# from io import BytesIO
# import random
# import time
# from telegram import ChatPermissions, ParseMode, Update
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, run_async
# import html
# import os
# from time import sleep
# from telegram import Update
# from telegram.error import BadRequest, RetryAfter, Unauthorized
# from telegram.ext import CallbackContext, CommandHandler, Filters
# from telegram.ext.dispatcher import run_async
# import time
# import datetime
# from requests import get
# from typing import List
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     RegexHandler,
# )
# from telegram import (
#     Update,
#     ParseMode,
#     MAX_MESSAGE_LENGTH,
# )
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, run_async
# from datetime import datetime
# from io import BytesIO
# from telegram import ParseMode, Update
# from telegram.error import BadRequest, TelegramError, Unauthorized
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# from telegram.utils.helpers import mention_html
# import bs4
# import requests
# import re
# from asyncio import sleep
# from telethon.events import NewMessage
# from telethon import events
# from telethon import types
# from telethon.tl import functions
# import html
# from telegram import Message, Chat, ParseMode, MessageEntity, Update
# from telegram import TelegramError, ChatPermissions
# from telegram.error import BadRequest
# from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters
# from telegram.ext.dispatcher import run_async
# from telegram.utils.helpers import mention_html
# from alphabet_detector import AlphabetDetector
# from datetime import datetime
# from functools import wraps
# from telegram.ext import CallbackContext
# from tswift import Song
# from telegram import Bot, Update, Message, Chat
# from telegram.ext import Updater, CommandHandler, CallbackContext, run_async
# from telegram.ext import CallbackContext, Filters, CommandHandler
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram import ParseMode, Update
# from telegram.ext.dispatcher import run_async
# from telegram.ext import CallbackContext, Filters, CommandHandler

# import collections
# from telegram import Update, ChatPermissions
# from telegram.error import BadRequest
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, CommandHandler, run_async
# from telegram.ext import CallbackContext, CommandHandler, run_async
# from telegram import Update
# from telegram.ext import CallbackContext, run_async
# import random
# from telegram import Update, Bot, ParseMode
# from telegram.ext import CommandHandler, CallbackContext, run_async
# import requests
# import re, ast
# from io import BytesIO
# import random
# from telegram import Bot, Chat, ChatPermissions, ParseMode, Update
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, CommandHandler, run_async
# from telegram.utils.helpers import mention_html
# import html
# from typing import Optional
# from typing import Optional
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, run_async
# from telegram import (
#     MAX_MESSAGE_LENGTH,
#     InlineKeyboardMarkup,
#     Message,
#     ParseMode,
#     Update,
#     InlineKeyboardButton,
# )
# from telegram.error import BadRequest
# from telegram.utils.helpers import escape_markdown, mention_markdown
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     CallbackQueryHandler,
#     Filters,
#     MessageHandler,
# )
# from telegram.ext.dispatcher import run_async
# import os
# from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
# from telegram.error import BadRequest, Unauthorized
# from telegram.ext import (
#     CallbackContext,
#     CallbackQueryHandler,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# from telegram.utils.helpers import mention_html
# import html
# import os
# import re
# import requests
# import urllib
# import urllib.request
# import urllib.parse
# from urllib.error import URLError, HTTPError
# from bs4 import BeautifulSoup
# from telegram import InputMediaPhoto, TelegramError
# from telegram import Update
# from telegram.ext import CallbackContext, run_async
# from typing import Optional
# from telegram import (
#     InlineKeyboardButton,
#     InlineKeyboardMarkup,
#     Message,
#     ParseMode,
#     Update,
#     User,
# )
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
# from telegram.utils.helpers import escape_markdown

# import sre_constants
# import regex
# from telegram import Update
# from telegram.ext import CallbackContext, Filters, run_async

# import telegram
# from telegram import Update
# from telegram.ext import CallbackContext, run_async
# import math
# import requests
# import urllib.request as urllib
# from PIL import Image
# from html import escape
# from bs4 import BeautifulSoup as bs
# from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram import TelegramError, Update
# from telegram.ext import run_async, CallbackContext
# from telegram.utils.helpers import mention_html
# import telegram
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, run_async
# import html
# from telegram.ext import CallbackContext, CommandHandler, run_async
# from datetime import datetime
# from platform import python_version, uname
# from telethon import version as tlthn
# from telegram import Update, Bot, Message, Chat, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, version as pybot
# from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler, Filters
# from telegram.ext.dispatcher import run_async
# from telegram.error import BadRequest, Unauthorized
# import os
# import subprocess
# import time
# import os
# import requests
# import speedtest
# import json
# import sys
# import traceback
# import psutil
# import platform
# import sqlalchemy
# from datetime import datetime
# from typing import List
# from gtts import gTTS
# from telegram import Update, ChatAction, ParseMode
# import requests
# import re
# import os
# import requests
# from telethon.tl.functions.channels import GetFullChannelRequest
# from telethon.tl.types import ChannelParticipantsAdmins
# from telethon import events
# from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update, MessageEntity
# from telegram.ext import CallbackContext, CommandHandler, Filters
# from telegram.ext.dispatcher import run_async
# from telegram.error import BadRequest
# from telegram.utils.helpers import escape_markdown, mention_html

# from io import BytesIO
# from time import sleep
# from telegram import TelegramError, Update
# from telegram.error import BadRequest, Unauthorized
# from telegram.ext import (
#     CallbackContext,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# import html
# import re
# from telegram import (
#     CallbackQuery,
#     Chat,
#     InlineKeyboardButton,
#     InlineKeyboardMarkup,
#     Message,
#     ParseMode,
#     Update,
#     User,
# )
# from telegram.error import BadRequest
# from telegram.ext import (
#     CallbackContext,
#     CallbackQueryHandler,
#     CommandHandler,
#     DispatcherHandlerStop,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# from typing import Optional
# import threading
# import json
# from datetime import datetime
# from pytz import country_timezones as c_tz, timezone as tz, country_names as c_n
# from requests import get
# from telegram import Bot, Update, ParseMode
# from telegram.ext import Updater, CommandHandler
# from telegram.ext import CallbackContext, run_async
# import html
# import random
# import re
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, run_async
# import time
# from functools import partial
# from contextlib import suppress
# import wikipedia, os, glob
# from telegram import ParseMode, Update
# from telegram.ext import CallbackContext, run_async
# from wikipedia.exceptions import DisambiguationError, PageError
# from telegram import MAX_MESSAGE_LENGTH, Bot, InlineKeyboardButton, ParseMode
# from telegram.error import TelegramError
# import threading
# from telegram.error import BadRequest
# from telegram.ext import (
#     CallbackContext,
#     CallbackQueryHandler,
#     CommandHandler,
#     Filters,
#     MessageHandler,
#     run_async,
# )
# from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown
# from asyncio import sleep
# from telethon import events
# import html
# from telegram import ParseMode, Update
# from telegram.error import BadRequest
# from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
# from telegram.utils.helpers import mention_html
# import logging
# import importlib
# import time
# import re
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
# from telegram.error import (
#     BadRequest,
#     ChatMigrated,
#     NetworkError,
#     TelegramError,
#     TimedOut,
#     Unauthorized,
# )
# from telegram.ext import (
#     CallbackContext,
#     CallbackQueryHandler,
#     CommandHandler,
#     Filters,
#     MessageHandler,
# )
# from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
# from telegram.utils.helpers import escape_markdown
# import os
# import sys
# import time
# import spamwatch
# import telegram.ext as tg
# from telethon import TelegramClient
# import threading
# import ast
# import threading
# from sqlalchemy import (
#     Column,
#     ForeignKey,
#     Integer,
#     String,
#     UnicodeText,
#     UniqueConstraint,
#     func,
# )
# import threading
# import random
# import threading
# from typing import Union
# from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText
# from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func
# from sqlalchemy.dialects import postgresql
# from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
# from telegram.error import BadRequest, Unauthorized
# from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func
# from typing import Union
# import regex
# from enum import IntEnum, unique
# from telegram import Message
# from sqlalchemy import func, distinct, Column, String, UnicodeText, Integer
# from time import sleep
# from typing import Dict, List
# import threading
# from sqlalchemy import Column, Integer, String, UnicodeText, distinct, func
# from sqlalchemy import Column, String, UnicodeText
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker
# from telegram import ChatAction, Update
# from telegram.ext import CallbackContext
# from time import perf_counter
# from functools import wraps
# import threading
# from sqlalchemy import Column, String, UnicodeText, Integer, func, distinct
# import threading
# from sqlalchemy import String, Column, Integer, UnicodeText
# from cachetools import TTLCache
# from threading import RLock
# from telegram import Chat, ChatMember, ParseMode, Update
# from telegram.ext import CallbackContext
# from typing import List, Optional
# from telegram import Message, MessageEntity
# from telegram.error import BadRequest
# from telegram import Message
# from telegram.ext import MessageFilter
# import urllib.request as url
# import json
# import datetime
# from telegram import Update
# from telegram.ext import CommandHandler, MessageHandler, Filters
# from pyrate_limiter import (
#     BucketFullException,
#     Duration,
#     RequestRate,
#     Limiter,
#     MemoryListBucket,
# )
# import threading
# from datetime import datetime

# from sqlalchemy import Boolean, Column, Integer, UnicodeText, DateTime
# import re
# import time
# from typing import Dict, List
# import bleach
# import markdown2
# import emoji
# from telegram import MessageEntity
# from telegram.utils.helpers import escape_markdown
# "========================================================================================================="