from sideloader import *
from SKARSHOTS.clear_cmd_sql import get_clearcmd
from SƈαɾLσɾԃ import dispatcher
from SKARS.TURNOFF import DisableAbleCommandHandler
from ꜰᴜɴᴄᴘᴏᴅ.misc import delete

__mod_name__ = "Talk 2 Speech"
TTS = TTS =__help__ = f"""{ALKL}
This is a module made to convert any text to speech.
Try it with funny words lol!

⚔️ •/talk <text>:
    convert text to speech
"""

def talk(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    delmsg = ""

    if message.reply_to_message:
        delmsg = message.reply_to_message.text

    if args:
        delmsg = "  ".join(args).lower()

        current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
        filename = datetime.now().strftime("%d%m%y-%H%M%S%f")
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        lang = "ml"
        talk = gTTS(delmsg, lang)
        talk.save("k.mp3")
        with open("k.mp3", "rb") as f:
            linelist = list(f)
            linecount = len(linelist)
        if linecount == 1:
            update.message.chat.send_action(ChatAction.RECORD_AUDIO)
            lang = "en"
            talk = gTTS(delmsg, lang)
            talk.save("k.mp3")
        with open("k.mp3", "rb") as speech:
            delmsg = update.message.reply_voice(speech, quote=False)

        os.remove("k.mp3")

    else:
        delmsg = message.reply_text(
        "Reply a message or give something like:\n`/talk <message>`",
        parse_mode = ParseMode.MARKDOWN
        )

    cleartime = get_clearcmd(chat.id, "talk")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


TTS_WORK = DisableAbleCommandHandler("talk", talk, run_async=True)
__handlers__ = [TTS_WORK]
dispatcher.add_handler(TTS_WORK)