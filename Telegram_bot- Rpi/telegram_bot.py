import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
#from picamera import PiCamera
#camera = PiCamera()

"""
After **inserting token** in the source code, run it:
```
$ python2.7 diceyclock.py
```
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""
def takepic():
    camera.start_preview()
    time.sleep(5)
    camera.capture('image.jpeg')
    camera.stop_preview()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command=='/who':
        bot.sendMessage(chat_id, 'I am ' + str(bot.getMe()['username']))
    elif command== '/help' or command=='?' or command=='/start':
        bot.sendMessage(chat_id,"/roll- random die roll\n/time--to get current time\n/who--to get name of the bot\n/info- to know more about the me\n/sendpic - sample pic")
    elif command== '/info':
        bot.sendMessage(chat_id,"I'm thriver bot created by Manodhayan")
    elif command== '/sendpic':
        #takepic()
        path='/home/pi/telegram-bot/image.jpeg'
        
        bot.sendPhoto(chat_id,open(path, 'rb'))
        #bot.sendPhoto(chat_id,'https://www.planwallpaper.com/static/images/magic-of-blue-universe-images.jpg')
        
bot = telepot.Bot('606668742:AAHWouhyPVoERH074rgY5tG-m3FYvfWq5qI')

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
