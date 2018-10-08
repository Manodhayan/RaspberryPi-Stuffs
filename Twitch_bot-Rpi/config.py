HOST = "irc.twitch.tv"              # This is Twitchs IRC server
PORT = 6667                         # Twitchs IRC server listens on port 6767
NICK = "YourUsername"            # Twitch username your using for your bot
PASS = "oauth:YourToken" # your Twitch OAuth token
CHAN = "#YourChannel"                   # the channel you want the bot to join.
RATE = (20/30) # messages per seccond
BAN_PAT = [
    r"swear",
    r"fuck",
]
