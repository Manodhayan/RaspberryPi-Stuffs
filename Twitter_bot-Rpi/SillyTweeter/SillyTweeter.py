#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'YourConsumerKey'
CONSUMER_SECRET = 'YourConsumerSecret'
ACCESS_KEY = 'YourAccesKey'
ACCESS_SECRET = 'YourAccessSecret'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
