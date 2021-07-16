from Deve import *
from Storeroom import *

def send_message(message, text, *args, **kwargs):
    try:
        return message.reply_text(text, *args, **kwargs)
    except BadRequest as err:
        if str(err) == "Reply message not found":
            return message.reply_text(text, quote=False, *args, **kwargs)

def typing_action(func):
    @wraps(func)
    def command_func(update: Update, context: CallbackContext, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING
        )
        return func(update, context, *args, **kwargs)
    return command_func

def location_action(func):
    @wraps(func)
    def command_func(update: Update, context: CallbackContext, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.FIND_LOCATION
        )
        return func(update, context, *args, **kwargs)
    return command_func

def voice_record_action(func):
    @wraps(func)
    def command_func(update: Update, context: CallbackContext, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.RECORD_VOICE
        )
        return func(update, context, *args, **kwargs)
    return command_func

def upload_document_action(func):
    @wraps(func)
    def command_func(update: Update, context: CallbackContext, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_DOCUMENT
        )
        return func(update, context, *args, **kwargs)
    return command_func