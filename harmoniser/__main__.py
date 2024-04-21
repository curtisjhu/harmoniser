import sys
import pyaudio
from .effects import *
from .constants import *
import numpy as np
from pynput import keyboard


p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

stream = p.open(format=pyaudio.paFloat32,
                channels=1 if sys.platform == 'darwin' else 2,
                rate=SAMPLE_RATE,
                input=True,
                output=True,
                input_device_index=2,
                frames_per_buffer=CHUNK)
# listener = keyboard.Listener(
#     on_press=on_press)
# listener.start()


print('* recording')

# Seems like latency is really an issue here
# Input overflow: some of the data was lost in between reads due to the latency

t = 0
while True:
    in_buffer = stream.read(CHUNK, exception_on_overflow=False) # as bytes

    buffer = np.frombuffer(in_buffer, dtype=np.float32) # as array of floats

    # AUDIO PROCESSING HERE 

    # buffer = major_chord(buffer)
    # buffer = frog(buffer)
    buffer = low_voice(buffer)
    # buffer = high_voice(buffer)
    # buffer = darth_vader(buffer)
    # buffer = low_pass(buffer)
    # buffer = low_pass(buffer)

    # AUDIO PROCESSING ENDS HERE 

    out_buffer = buffer.tobytes()
    stream.write(out_buffer)

    t += 0.001

print('* done')


stream.close()
p.terminate()