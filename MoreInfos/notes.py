NOTES =  """
 • `/get <notename>`*:* get the note with this notename
 • `#<notename>`*:* same as /get
 • `/notes` or `/saved`*:* list all saved notes in this chat
 • `/number` *:* Will pull the note of that number in the list
If you would like to retrieve the contents of a note without any formatting, use `/get <notename> noformat`. This can \
be useful when updating a current note

*Admins only:*
 • `/save <notename> <notedata>`*:* saves notedata as a note with name notename
A button can be added to a note by using standard markdown link syntax - the link should just be prepended with a \
`buttonurl:` section, as such: `[somelink](buttonurl:example.com)`. Check `/markdownhelp` for more info
 • `/save <notename>`*:* save the replied message as a note with name notename
 Separate diff replies by `%%%` to get random notes
 *Example:* 
 `/save notename
 Reply 1
 %%%
 Reply 2
 %%%
 Reply 3`
 • `/clear <notename>`*:* clear note with this name
 • `/removeallnotes`*:* removes all notes from the group
 *Note:* Note names are case-insensitive, and they are automatically converted to lowercase before getting saved.
 • `/privatenotes <on/yes/1/off/no/0>`: enable or disable private notes in chat
"""