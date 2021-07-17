FILTERS = __Hype_More__ = """
 • `/filters`*:* List all active filters saved in the chat.

*Admin only:*
 • `/filter <keyword> <reply message>`*:* Add a filter to this chat. The bot will now reply that message whenever 'keyword'\
is mentioned. If you reply to a sticker with a keyword, the bot will reply with that sticker. NOTE: all filter \
keywords are in lowercase. If you want your keyword to be a sentence, use quotes. eg: /filter "hey there" How you \
doin?
 Separate diff replies by `%%%` to get random replies
 *Example:* 
 `/filter "filtername"
 Reply 1
 %%%
 Reply 2
 %%%
 Reply 3`
 • `/stop <filter keyword>`*:* Stop that filter.

*Chat creator only:*
 • `/removeallfilters`*:* Remove all chat filters at once.

*Note*: Filters also support markdown formatters like: {first}, {last} etc.. and buttons.
Check `/markdownhelp` to know more!

"""