# https://librosa.org/doc/latest/effects.html#effects

import librosa
from .constants import *

def harmonizer(chunk):
	# read the keyboard input
	# pitch shift into those midi
	librosa.effects.pitch_shift(chunk, sr=SAMPLE_RATE, n_steps=3)
	return chunk
	

# Live?
# audio separation
# https://pytorch.org/audio/main/tutorials/hybrid_demucs_tutorial.html
