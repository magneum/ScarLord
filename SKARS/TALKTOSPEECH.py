from sideloader import *
from SKARSHOTS.clear_cmd_sql import get_clearcmd
from SƈαɾLσɾԃ import dispatcher
from SKARS.TURNOFF import DisableAbleCommandHandler
from ꜰᴜɴᴄᴘᴏᴅ.misc import delete

__mod_name__ = "Talk 2 Speech"
TTS = TTS =__help__ = f"""{ALKL}
This is a module made to convert any english text to speech.
Try it with funny words lol!

⚔️ •/talk | /speak | /tts | /t <text>:
    convert text to speech  
"""

US = f"""{ALKL}
Sent via :@HVScarlordBot
GitHub:@HypeVoidBot"""

def talk(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    chat = update.effective_chat
    delmsg = ""

    if message.reply_to_message:
        delmsg = message.reply_to_message.text

    if args:
        delmsg = "  ".join(args).lower()
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        lang = "ml"
        talk = gTTS(delmsg, lang)
        talk.save("HypeVoidSoulTalks.mp3")
        with open("HypeVoidSoulTalks.mp3", "rb") as f:
            linelist = list(f)
            linecount = len(linelist)
        if linecount == 1:
            update.message.chat.send_action(ChatAction.RECORD_AUDIO)
            message.reply_text(
            "✨Please Wait...\nMight take few seconds due to heavy usage of this module.",
            parse_mode = ParseMode.MARKDOWN)
            asyncio.sleep(2)
            lang = "en"
            talk = gTTS(delmsg, lang)
            talk.save("HypeVoidSoulTalks.mp3")
        music = open(
        "HypeVoidSoulTalks.mp3",
        "rb")
        delmsg = update.message.reply_voice(music, caption=US,quote=False)
        os.remove("HypeVoidSoulTalks.mp3")
    else:
        delmsg = message.reply_text(
        f"""{ALKL}Reply a message or give something like\n⚔️ •/talk | /speak | /tts | /t <text>:""",
        parse_mode = ParseMode.MARKDOWN)
    cleartime = get_clearcmd(chat.id, "talk")
    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


TTS_WORK = DisableAbleCommandHandler(["talk", "speak", "tts", "t"], talk, run_async=True)
__handlers__ = [TTS_WORK]
dispatcher.add_handler(TTS_WORK)