#!/usr/bin/env python3

import aiy.audio  
import aiy.voicehat
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random

foo = ['Ciao bello, Buon Giorno', 'come stai ragazzo?', 'uno, due, tre, quattro, cinque, sei, sette, otto, nove, dieci', 'che vuoi fare oggi?', 'cinque, sei, sette, otto','sopra la panca la capra campa, sotto la panca la capra crepa',
     'sai parlare Itaaliano?', 'hey Maambo, Maambo Italiano', 'Miinchia, braavo',
      'Sopra la panca la capra campa, sotto la panca la capra crepa', 'Michele aveva un gallo, bianco rosso e verde e giallo, e per farlo ben cantare, gli dava da mangiare']


button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()

#path to wave file
path2 = '/home/pi/audio/1523749823.wav'
pp =    '/home/pi/audio/leo.wav'

#play audio when button is pressed
def say(words):
	aiy.audio.say(words, lang='it-IT', volume=20)


def audio():
	print('Playing a test sound...')
	aiy.audio.say('Buon Giorno, principe',lang='it-IT', volume=20,pitch=105)
	#aiy.audio.play_wave(pp)
	aiy.audio.say('Ciao Bella', lang='it-IT', volume=20)

while True:
	button.wait_for_press()
	led.set_state(aiy.voicehat.LED.ON)
	say(random.choice(foo))
	led.set_state(aiy.voicehat.LED.OFF)


