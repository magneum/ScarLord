__Hype_More__ = """
*Available commands:*\n
*Covid:*
 • `/covid <country>`: provides lastest covid information\n
*Weather:*
 • `/weather <city>`: gives weather information about a specific location or country\n
*Quotly:*
 • `/quotly`: reply to a message to get a quoted message\n
*Markdown:*
 • `/markdownhelp`*:* quick summary of how markdown works in telegram - can only be called in private chats\n
*Paste:*
 • `/paste`*:* saves replied content to `nekobin.com` and replies with a url\n
*React:*
 • `/react`*:* reacts with a random reaction\n
*Urban Dictonary:*
 • `/ud <word>`*:* type the word or expression you want to search use\n
*Wikipedia:*
 • `/wiki <query>`*:* wikipedia your query\n
*Wallpapers:*
 • `/wall <query>`*:* get a wallpaper from wall.alphacoders.com\n
*Currency converter:* 
 • `/cash`*:* currency converter
Example:
 `/cash 1 USD INR`  
      _OR_
 `/cash 1 usd inr`
Output: `1.0 USD = 75.505 INR`\n
*Timezones:*
 • `/time <query>`*:* Gives information about a timezone.
*Available queries:* Country Code/Country Name/Timezone Name
• 🕐 [Timezones list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
"""

MARKDOWN_HELP = f"""
Markdown is a very powerful formatting tool supported by telegram. SƈαɾLσɾԃ has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

• <code>_italic_</code>: wrapping text with '_' will produce italic text
• <code>*bold*</code>: wrapping text with '*' will produce bold text
• <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
• <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
<b>Example:</b><code>[test](example.com)</code>

• <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.

Keep in mind that your message <b>MUST</b> contain some text other than just a button!
"""