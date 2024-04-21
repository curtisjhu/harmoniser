# https://librosa.org/doc/latest/effects.html#effects

import librosa
from .constants import *
import numpy as np

def harmoniser(chunk):
	# read the keyboard input
	# pitch shift into those midi
	chunk = librosa.effects.pitch_shift(chunk, sr=SAMPLE_RATE, n_steps=4)
	return chunk
	

def frog(buffer):
	freqs = librosa.stft(buffer)
	# pitch, decibels is base 2
	# A is amplitude which controls loudness
	# Ae^{k * -ix}
	A = np.abs(freqs)
	phase = np.angle(freqs)
	freqs = A*np.exp(phase * -1j)

	buffer = librosa.istft(freqs)
	return buffer


def separate(A, phase):
	return 0

# Live?
# audio separation
# https://pytorch.org/audio/main/tutorials/hybrid_demucs_tutorial.html
