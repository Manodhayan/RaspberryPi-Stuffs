#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'ZEl5LkbNnjXGdY9MEcP5bIVVY'
CONSUMER_SECRET = 'u63gTWJ7vL5AHpR5dSW3GHU6fYGLw8wz5jY1wWoSx68qCTmSOS'
ACCESS_KEY = '2327212614-9uqCRgSlStR6SpYbtEnyeUT7pEoEHFNCMtQfh7i'
ACCESS_SECRET = 'D5VZyjdhsID1qKJsCLNb5imXiZdItezgrOgH7fn1jr7Jt'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
