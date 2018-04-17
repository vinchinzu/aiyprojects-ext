import aiy.audio  
import aiy.voicehat
import aiy.cloudspeech
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random

foo = ['Ciao bello', 'Buon Giorno', 'come stai ragazzo?', 'uno, due, tre, quattro, cinque, sei', 'che vuoi fare oggi?', 'cinque, sei, sette, otto','sopra la panca la capra campa, sotto la panca la capra crepa',
     'sai parlare italiano', 'hey mambo, mambo italiano', 'minchia, bravo']


button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()

TEST_SOUND_PATH = '/usr/share/sounds/alsa/Front_Center.wav'

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



