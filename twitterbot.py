#A twitter bot to find a users latest tweet, and repost a modified version based on user preferences. In Python 2.7
#Written by Jason Bernier
#https://github.com/jasonbernier

import re
import twitter
import sys

api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')

#To see if your credentials are successful:
print(api.VerifyCredentials())

twitteruser = raw_input("Enter the Twitter User name you are looking to repost: ") #username to follow/post
wordchange = raw_input("Enter the word you want to repost with: ")
twitteruserstatus = api.GetUserTimeLine(twitteruser)
#Check for the word Science in any case and replace it with your word.. this should probably be edited for your needs
newstatusupdate = re.sub (r'[Ss][Cc][Ii][Ee][Nn][Cc][Ee]',wordchange)
status= api.Postupdate(newstatusupdate)

