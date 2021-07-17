__Hype_More__ = """
*Get module configuration:*
• `/clearcmd`: provides all commands that has been set in current group with their deletion time
• `/clearcmd list`: list all available commands for this module
• `/clearcmd <command>`: get the deletion time for a specific `<command>`

*Set module configuration:*
• `/clearcmd <command> <time>`: set a deletion `<time>` for a specific `<command>` in current group. All outputs of that command will be deleted in that group after time value in seconds. Time can be set between 5 and 300 seconds

*Restore module configuration:*
• `/clearcmd restore`: the deletion time set for ALL commands will be removed in current group
• `/clearcmd <command> restore`: the deletion time set for a specific `<command>` will be removed in current group
"""