from Storeroom import *

SED = __Hype_More__ = """
 • `s/<text1>/<text2>(/<flag>)`*:* Reply to a message with this to perform a sed operation on that message, replacing all \
occurrences of 'text1' with 'text2'. Flags are optional, and currently include 'i' for ignore case, 'g' for global, \
or nothing. Delimiters include `/`, `_`, `|`, and `:`. Text grouping is supported. The resulting message cannot be \
larger than {}.
*Reminder:* Sed uses some special characters to make matching easier, such as these: `+*.?\\`
If you want to use these characters, make sure you escape them!
*Example:* \\?.
""".format(
    telegram.MAX_MESSAGE_LENGTH
)