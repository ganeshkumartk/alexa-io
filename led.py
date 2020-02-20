#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:17:43 2020

@author: Ganesh Kumar
"""

from Adafruit_IO import *
import RPi.GPIO as G
import time
aio = Client('YOUR_AIO_USERNAME', 'YOUR_AIO_KEY')
G.setmode(G.BCM)
G.setup(18,G.OUT)                     #LED connected at GPIO Pin 18 
try:
	digital = aio.feeds('led')
except RequestError:                  #Checks if Corresponding feed is present in Adafruit IO else, creates newly.
	feed = Feed(name='led')
	digital = aio.create_feed(feed)
	data = aio.feeds('led')

while True:                            #Recieve Triggers from Dashboard via Alexa
	data = aio.receive(digital.key)
	if data.value == 'ON':
		G.output(18,G.HIGH)
		print("Received LED on")
	elif data.value == 'OFF':
		print("Received LED off")
		G.output(18,G.LOW)

time.sleep(1)
