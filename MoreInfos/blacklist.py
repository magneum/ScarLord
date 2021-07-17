__Hype_More__ = """

Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!

*NOTE*: Blacklists do not affect group admins.

 • `/blacklist`*:* View the current blacklisted words.

Admin only:
 • `/addblacklist <triggers>`*:* Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
 • `/unblacklist <triggers>`*:* Remove triggers from the blacklist. Same newline logic applies here, so you can remove multiple triggers at once.
 • `/blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>`*:* Action to perform when someone sends blacklisted words.

Blacklist sticker is used to stop certain stickers. Whenever a sticker is sent, the message will be deleted immediately.
*NOTE:* Blacklist stickers do not affect the group admin
 • `/blsticker`*:* See current blacklisted sticker
*Only admin:*
 • `/addblsticker <sticker link>`*:* Add the sticker trigger to the black list. Can be added via reply sticker
 • `/unblsticker <sticker link>`*:* Remove triggers from blacklist. The same newline logic applies here, so you can delete multiple triggers at once
 • `/rmblsticker <sticker link>`*:* Same as above
 • `/blstickermode <delete/ban/tban/mute/tmute>`*:* sets up a default action on what to do if users use blacklisted stickers
Note:
 • `<sticker link>` can be `https://t.me/addstickers/<sticker>` or just `<sticker>` or reply to the sticker message

"""