import sys
import pyaudio
from .effects import *
from .constants import *
import numpy as np


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1 if sys.platform == 'darwin' else 2,
                rate=SAMPLE_RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)


print('* recording')

while True:
    buffer = stream.read(CHUNK)
    # audio processing here
    arr = np.frombuffer(buffer, dtype=np.float32)
    arr = harmonizer(arr)

    buffer = arr.tobytes()
    stream.write(buffer)

print('* done')


stream.close()
p.terminate()