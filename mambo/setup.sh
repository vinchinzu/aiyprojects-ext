#!/bin/bash

youtube-dl --extract-audio --audio-format mp3 --output mambo.mp3 https://www.youtube.com/watch?v=UM1BYWEF3vY

ffmpeg -i mambo.mp3 -acodec pcm_s16le -ac 1 -ar 16000 mambo.wav

rm mambo.mp3
