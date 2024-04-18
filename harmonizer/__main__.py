import sys
import pyaudio
from .effects import *
from .constants import *
import numpy as np


p = pyaudio.PyAudio()
dtype = p.get_format_from_width(2)
stream = p.open(format=dtype,
                channels=1 if sys.platform == 'darwin' else 2,
                rate=SAMPLE_RATE,
                input=True,
                output=True,
                frames_per_buffer=BUFFER_SIZE)


print('* recording')

while True:
    buffer = stream.read(BUFFER_SIZE)
    # audio processing here
    array = np.frombuffer(buffer, dtype='int16')
    array = harmonizer(array)

    buffer = array.tobytes()
    stream.write(buffer)

print('* done')


stream.close()
p.terminate()