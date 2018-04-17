# Record wave file and play it back, timestamping and saving into directory
#TODO
# Add new folder for audio outside of git,
# clean imports

import fileinput
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import traceback
import time
import datetime
import aiy.audio 
from aiy._drivers._hat import get_aiy_device_name

RECORD_DURATION_SECONDS = 3

def record():
    temp_file, temp_path = tempfile.mkstemp(suffix='.wav')
    os.close(temp_file)
    ts = int(time.time())
    file = str(ts) + ".wav"
    
    try:
        input("When you're ready, press enter and say a phrase ...")
        print('Recording...')
        #aiy.audio.record_to_wave(temp_path, RECORD_DURATION_SECONDS)
        aiy.audio.record_to_wave(file, RECORD_DURATION_SECONDS)
        print('Playing back recorded audio...')
       #aiy.audio.play_wave(temp_path)
        aiy.audio.play_wave(file)

    finally:
        try:
            os.unlink(temp_path)
        except FileNotFoundError:
            pass

    return ask('Did you hear your own voice?')



def ask(prompt):
    """Get a yes or no answer from the user."""
    ans = input(prompt + ' (y/n) ')

    while not ans or ans[0].lower() not in 'yn':
        ans = input('Please enter y or n: ')

    return ans[0].lower() == 'y'





def main():

    record()


if __name__ == '__main__':
    try:
        main()
        input('Press Enter to close...')
    except Exception: 
        traceback.print_exc()
        input('Press Enter to close...')

