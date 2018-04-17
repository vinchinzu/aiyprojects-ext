
from gtts import gTTS
tts = gTTS(text = "Buon Giorno Principe, Leonardo", lang='it')

tts.save("leo.mp3")


subprocess.call(['ffmpeg', '-i', 'leo.mp3','-acodec','pcm_s16le','-ac','1', '-ar','16000',
	'leo.wav'])

