#!/usr/bin/env python3

import aiy.audio
import aiy.voicehat
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random

phrase_list = ['Ciao bello, Buon Giorno', 'come stai ragazzo?', 'uno, due, tre, quattro, cinque, sei, sette, otto, nove, dieci', 'che vuoi fare oggi?', 'cinque, sei, sette, otto','sopra la panca la capra campa, sotto la panca la capra crepa',
     'sai parlare Itaaliano?', 'heeeey Maambo, Maambo Itaaaliano', 'Miinchia, braavo',
      'Sopra la panca la capra campa, sotto la panca la capra crepa', 'Michele aveva un gallo, bianco rosso e verde e giallo, e per farlo ben cantare, gli dava da mangiare',
	      'Certo']

button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()

#play audio when button is pressed
def say_italian(words):
	aiy.audio.say(words, lang='it-IT', volume=20, pitch=100)

while True:
	button.wait_for_press()
	led.set_state(aiy.voicehat.LED.ON)
	say_italian(random.choice(phrase_list))
	led.set_state(aiy.voicehat.LED.OFF)



