
important => tagging the bot means using a message that would start with @ouroboros translator so that the bot knows that you are addressing it ( this also prevents confusions )

# Bot setup

## initialising a channel

1) user tags bot in a channel and sends message "translate here"
2) bot replies with acknowledgment message "will start translating here"
3) bot uses settings to know who to translate automatically and what to ignore

## removing a channel

1) user tags bot with message "stop translating here"
2) bot no longer translates message in channel

## setting up a user preference

1) user will tag the bot with flags separated from an arrow ( ex : ":flag_fr: => :flag_us:" )
2) the bot will set up the user preferences to the specifications ( french to english in this example )

## removing all preference

1) user tags bot with message "stop translating me"
2) bot removes user preference ( channel + user + lang )

# Bot usage

## asking for instructions

1) user asks for a list of possible instructions with message "instruction list" or "help"
2) bot outputs all of the possible instructions
3) bot outputs all of the managed languages

## asking for status

1) user asks for the general status of the bot
2) bot will reply with api status ( google translate ) and will tell if any issues are encountered

## user writes a message ( automatic translation )

1) if channel + user + user preferences have been saved then :
2) bot uses the google trad API in order to translates the message and replies to the user with the translation

## user writes a message ( translation request )

1) if channel has been saved
2) if message starts with flag
3) if message ends with flag list
4) translate message from first flag to end flags

## error management

1) if a flag is not in flag list => ignore it
