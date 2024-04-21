# https://librosa.org/doc/latest/effects.html#effects

import librosa
from .constants import *
import numpy as np

def harmoniser(buffer):
	# read the keyboard input
	# pitch shift into those midi
	buffer = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=4)
	return buffer

def major_chord(buffer):
	fundamental = buffer
	major_third = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=4)
	fifth = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=7)
	return fundamental + major_third + fifth

def minor_chord(buffer):
	fundamental = buffer
	minor_third = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=3)
	fifth = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=7)
	return fundamental + minor_third + fifth

def fifth(buffer):
	buffer = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=7)
	return buffer

def low_voice(buffer):
	buffer = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=-7)
	return buffer

def high_voice(buffer):
	buffer = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=12)
	return buffer

def doppler_effect(buffer):
	buffer = librosa.effects.pitch_shift(buffer, sr=SAMPLE_RATE, n_steps=-1)
	return buffer

def darth_vader(buffer):
	buffer = low_voice(buffer)
	buffer = frog(buffer)
	return buffer

def batman(buffer):
	buffer = low_voice(buffer)
	return buffer

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

def low_pass(buffer, f=1000):
	freqs = librosa.stft(buffer)

	# cutoff = np.linspace(1, , num=freqs.shape[0], base=2.0)
	# cutoff = [1/(1 + np.exp(x)) for x in range(freqs.shape[0])]
	cutoff = np.ones(freqs.shape[0])
	A = np.abs(freqs)

	# multiply across
	B = (A.T * cutoff).T 

	phase = np.angle(freqs)

	freqs = A*np.exp(phase * 1j)

	buffer = librosa.istft(freqs)
	return buffer

def high_pass(buffer):
	freqs = librosa.stft(buffer)

	# cutoff = np.linspace(1, , num=freqs.shape[0], base=2.0)
	# cutoff = [1/(1 + np.exp(x)) for x in range(freqs.shape[0])]
	cutoff = np.ones(freqs.shape[0])
	A = np.abs(freqs)

	# multiply across
	B = (A.T * cutoff).T 

	phase = np.angle(freqs)
	freqs = A*np.exp(phase * 1j)

	buffer = librosa.istft(freqs)
	return buffer

def old_phonograph(buffer):
	freqs = librosa.stft(buffer)
	A = np.abs(freqs)

	phase = np.angle(freqs)

	freqs = np.tanh(A*np.exp(phase * 1j))

	buffer = librosa.istft(freqs)
	return buffer

def distortion(buffer, gain=3):
	freqs = librosa.stft(buffer)
	A = np.abs(freqs)

	phase = np.angle(freqs)

	freqs = np.tanh(gain*A*np.exp(phase * 1j))

	buffer = librosa.istft(freqs)
	return buffer



def separate(A, phase):
	return 0

# Live?
# audio separation
# https://pytorch.org/audio/main/tutorials/hybrid_demucs_tutorial.html
