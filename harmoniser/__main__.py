import sys
import pyaudio
from .effects import *
from .constants import *
import numpy as np
from pynput import keyboard


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1 if sys.platform == 'darwin' else 2,
                rate=SAMPLE_RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)
# listener = keyboard.Listener(
#     on_press=on_press)
# listener.start()


print('* recording')

# Seems like latency is really an issue here
# Input overflow: some of the data was lost in between reads due to the latency

while True:
    buffer = stream.read(CHUNK, exception_on_overflow=False)
    # audio processing here
    arr = np.frombuffer(buffer, dtype=np.float32)

    # freq, detection, probabilities = librosa.pyin(arr, fmin=librosa.note_to_hz('E2'), fmax=librosa.note_to_hz('A5'), sr=SAMPLE_RATE, frame_length=CHUNK)
    harmonic, percussive = librosa.effects.hpss(arr)

    buffer = percussive.tobytes()
    stream.write(buffer)

print('* done')


stream.close()
p.terminate()