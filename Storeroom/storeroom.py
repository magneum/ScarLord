from telegram.error import BadRequest
from functools import wraps
import importlib
import html
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup
from requests import get
from telegram import Bot, Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import CallbackContext, run_async
from ujson import loads
from yaml import load, Loader
from typing import Optional, List
import re
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram import Message, Chat, Update, User, ChatPermissions
from telegram.utils.helpers import mention_html, escape_markdown
import json, time, os
from io import BytesIO
from telegram.ext import CallbackContext, run_async, CallbackQueryHandler
import html
from telegram import ParseMode, Message, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest
import importlib
import html
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
import os
import html
import html
from typing import Optional
from telegram import Chat, Message, ParseMode, Update, User, ChatPermissions
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html, mention_markdown
import re
from telegram import ParseMode, ChatPermissions, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters, run_async
from telegram.utils.helpers import mention_html

from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
import html
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler, run_async
import time
import re
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update, Bot
from telegram.error import BadRequest, Unauthorized
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, run_async
import requests
import subprocess
import sys
import re
import random
from html import escape
import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, InlineKeyboardButton, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    DispatcherHandlerStop,
    CallbackQueryHandler,
    run_async,
    Filters,
)
from telegram.utils.helpers import mention_html, escape_markdown
from contextlib import suppress
from time import sleep
from telegram import TelegramError, Update
from telegram.error import Unauthorized
from telegram.ext import CallbackContext, CommandHandler, run_async
from typing import Union
from telegram import ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    RegexHandler,
)
from future.utils import string_types
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler
import html
import traceback
import requests
from telegram.utils.helpers import escape_markdown
import html
import random
import traceback
import sys
import pretty_errors
import io
import ast
import csv
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler, run_async
import io
import os
import textwrap
import traceback
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MessageEntity,
    ParseMode,
    Update,
)
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    run_async,
)
from telegram.utils.helpers import mention_html, mention_markdown
import json
import os
import re
import time
import uuid
from io import BytesIO
import random
import time
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async
import html
import os
from time import sleep
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
import time
import datetime
from requests import get
from typing import List
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    RegexHandler,
)
from telegram import (
    Update,
    ParseMode,
    MAX_MESSAGE_LENGTH,
)
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from datetime import datetime
from io import BytesIO
from telegram import ParseMode, Update
from telegram.error import BadRequest, TelegramError, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
import bs4
import requests
import re
from asyncio import sleep
from telethon.events import NewMessage
from telethon import events
from telethon import types
from telethon.tl import functions
import html
from telegram import Message, Chat, ParseMode, MessageEntity, Update
from telegram import TelegramError, ChatPermissions
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, CallbackContext, Filters
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html
from alphabet_detector import AlphabetDetector
from datetime import datetime
from functools import wraps
from telegram.ext import CallbackContext
from tswift import Song
from telegram import Bot, Update, Message, Chat
from telegram.ext import Updater, CommandHandler, CallbackContext, run_async
from telegram.ext import CallbackContext, Filters, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

import collections
from telegram import Update, ChatPermissions
from telegram.error import BadRequest
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram import Update
from telegram.ext import CallbackContext, run_async
import random
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, CallbackContext, run_async
import requests
import re, ast
from io import BytesIO
import random
from telegram import Bot, Chat, ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html
import html
from typing import Optional
from typing import Optional
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from telegram import (
    MAX_MESSAGE_LENGTH,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    InlineKeyboardButton,
)
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_markdown
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import run_async
import os
from telegram import Chat, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
import html
import os
import re
import requests
import urllib
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from telegram import InputMediaPhoto, TelegramError
from telegram import Update
from telegram.ext import CallbackContext, run_async
from typing import Optional
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown

import sre_constants
import regex
from telegram import Update
from telegram.ext import CallbackContext, Filters, run_async

import telegram
from telegram import Update
from telegram.ext import CallbackContext, run_async
import math
import requests
import urllib.request as urllib
from PIL import Image
from html import escape
from bs4 import BeautifulSoup as bs
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import TelegramError, Update
from telegram.ext import run_async, CallbackContext
from telegram.utils.helpers import mention_html
import telegram
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
import html
from telegram.ext import CallbackContext, CommandHandler, run_async
from datetime import datetime
from platform import python_version, uname
from telethon import version as tlthn
from telegram import Update, Bot, Message, Chat, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, version as pybot
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler, Filters
from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest, Unauthorized
import os
import subprocess
import time
import os
import requests
import speedtest
import json
import sys
import traceback
import psutil
import platform
import sqlalchemy
from datetime import datetime
from typing import List
from gtts import gTTS
from telegram import Update, ChatAction, ParseMode
import requests
import re
import os
import os
import re
import requests
import urllib
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import requests
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events
from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update, MessageEntity
from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown, mention_html

from io import BytesIO
from time import sleep
from telegram import TelegramError, Update
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
import html
import re
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    DispatcherHandlerStop,
    Filters,
    MessageHandler,
    run_async,
)
from typing import Optional
import threading
import json
from datetime import datetime
from pytz import country_timezones as c_tz, timezone as tz, country_names as c_n
from requests import get
from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackContext, run_async
import html
import random
import re
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
import time
from functools import partial
from contextlib import suppress
import wikipedia, os, glob
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from wikipedia.exceptions import DisambiguationError, PageError
from telegram import MAX_MESSAGE_LENGTH, Bot, InlineKeyboardButton, ParseMode
from telegram.error import TelegramError
import threading
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown
from asyncio import sleep
from telethon import events
import html
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import mention_html
import logging
import importlib
import time
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
import os
import sys
import time
import spamwatch
import telegram.ext as tg
from telethon import TelegramClient
import threading
import ast
import threading
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
)
import threading
import random
import threading
from typing import Union
from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, distinct, func
from sqlalchemy.dialects import postgresql
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from telegram.error import BadRequest, Unauthorized
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func
from typing import Union
import regex
from enum import IntEnum, unique
from telegram import Message
from sqlalchemy import func, distinct, Column, String, UnicodeText, Integer
from time import sleep
from typing import Dict, List
import threading
from sqlalchemy import Column, Integer, String, UnicodeText, distinct, func
from sqlalchemy import Column, String, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from telegram import ChatAction, Update
from telegram.ext import CallbackContext
from time import perf_counter
from functools import wraps
import threading
from sqlalchemy import Column, String, UnicodeText, Integer, func, distinct
import threading
from sqlalchemy import String, Column, Integer, UnicodeText
from cachetools import TTLCache
from threading import RLock
from telegram import Chat, ChatMember, ParseMode, Update
from telegram.ext import CallbackContext
from typing import List, Optional
from telegram import Message, MessageEntity
from telegram.error import BadRequest
from telegram import Message
from telegram.ext import MessageFilter
import urllib.request as url
import json
import datetime
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters
from pyrate_limiter import (
    BucketFullException,
    Duration,
    RequestRate,
    Limiter,
    MemoryListBucket,
)
import threading
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, UnicodeText, DateTime
import re
import time
from typing import Dict, List
import bleach
import markdown2
import emoji
from telegram import MessageEntity
from telegram.utils.helpers import escape_markdown
