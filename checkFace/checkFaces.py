#!/usr/bin/env python3

import threading
import requests
import time
import httplib2
import time

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

threads = []

def play_mambo():
    aiy.audio.play_wave("/home/pi/aiyprojects-ext/mambo.wav")

def main():
    while True:
        print('Waiting for faces...')
        number = 0
        while number == 0:
             resp, content = httplib2.Http().request("http://10.0.0.36:9000/face_count.txt")
             number = int(content)
             print('num_faces=%d' % number)
             time.sleep(1)
        print('Got a face.')
        task = threading.Thread(target=play_mambo)
        threads.append(task)
        task.start()
        
        #text = recognizer.recognize()
        #if text is None:
        #    print('Sorry, I did not hear you.')
        #else:
        #    print('You said "', text, '"')
        #    if 'weather' in text:
        #        show_weather()
        #    if 'fairest' in text:
        #        aiy.audio.say('Over the seven jewelled hills, beyond the seventh fall, in the cottage of the seven dwarfs, dwells Snow White, fairest one of all.')

if __name__ == '__main__':
    main()
