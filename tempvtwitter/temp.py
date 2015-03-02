# -*- coding: utf-8 -*-
# Python3
# thanks to freenode/#crude/ravioli for the help
import subprocess
import time
import random
from twitter import OAuth, Twitter
from auth import *
from names import *

#Specify the twitter Oauth shitte
t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

#Get the temp from the command
temp = float(subprocess.check_output("/usr/bin/temperv14 -f", shell=True))

#Get the current time
time = time.strftime("%m-%d-%y at %H:%M")

#Make our statements we want to tweet by random
rand_cold = ['{2} Dude, its effin {1} in your office!', '{2} Its {1}, colder than a witches titty.']
rand_nice = ['{2}... my bro, its nice in your office: only {1} degrees', '{2} Hey man, nice day ahead, only {1} in your office']
rand_hot = ['{2} You are going to sweat your balls off today its already {1} in your office', '{2} Jesus titties its already {1} in your office']

#Put everything all together to tweet it
final_cold = random.choice(rand_cold).format(time, float(temp), twitter_names)
final_nice = random.choice(rand_nice).format(time, float(temp), twitter_names)
final_hot = random.choice(rand_hot).format(time, float(temp), twitter_names)

#Detect the temp sentance we want to
if temp <=float(60):
        t.statuses.update(status=final_cold)
#print checks to verify we're outputting to twitter correctly
#        print(final_cold)
#        print('Checkbit: {0} Cold'.format(float(temp)))
elif temp <=float(72):
        t.statuses.update(status=final_nice)
#print checks to verify we're outputting to twitter correctly
#        print(final_nice)
#        print('Checkbit:{0} Nice'.format(float(temp)))
else:
        t.statuses.update(status=final_hot)
#print checks to verify we're outputting to twitter correctly
#        print(final_hot)
#        print('Checkbit:{0} Hot'.format(float(temp)))