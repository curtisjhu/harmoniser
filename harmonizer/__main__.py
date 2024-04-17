import sys
import pyaudio

CHUNK = 1024 # 2^10
RATE = 44100

# Live?
# audio separation
# https://pytorch.org/audio/main/tutorials/hybrid_demucs_tutorial.html



p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(2),
                channels=1 if sys.platform == 'darwin' else 2,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)


print('* recording')

while True:
	chunk = stream.read(CHUNK)

	# audio processing here


	stream.write(chunk)

print('* done')


stream.close()
p.terminate()