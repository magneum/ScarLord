WARNS =  """
 • `/warns <userhandle>`*:* get a user's number, and reason, of warns.
 • `/warnlist`*:* list of all current warning filters

*Admins only:*
 • `/warn <userhandle>`*:* warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
 • `/dwarn <userhandle>`*:* warn a user and delete the message. After 3 warns, the user will be banned from the group. Can also be used as a reply.
 • `/resetwarn <userhandle>`*:* reset the warns for a user. Can also be used as a reply.
 • `/addwarn <keyword> <reply message>`*:* set a warning filter on a certain keyword. If you want your keyword to \
be a sentence, encompass it with quotes, as such: `/addwarn "very angry" This is an angry user`.
 • `/nowarn <keyword>`*:* stop a warning filter
 • `/warnlimit <num>`*:* set the warning limit
 • `/strongwarn <on/yes/off/no>`*:* If set to on, exceeding the warn limit will result in a ban. Else, will just punch.
"""