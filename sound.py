
import numpy as np
import time
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
import pickle
import peakutils

fs = 44100

number_table =	{
  "0": [941,1336],
  "1": [697,1209],
  "2": [697,1336],
  "3": [697,1477],
  "4": [770,1209],
  "5": [770,1336],
  "6": [770,1477],
  "7": [852,1209],
  "8": [852,1336],
  "9": [852,1477]
}

amplitude = 1
fs = 44100
t = 1

def generateSin(freq, amplitude, time, fs):
	n = time*fs
	x = np.linspace(0.0, time, n)
	s = amplitude*np.sin(freq*x*2*np.pi)
	return (x, s)


def play(data):

	#sd.default.samplerate = 44100
	fs = 44100
	#data = np.random.uniform(-5, 1, fs)
	sd.play(data, fs)
	time.sleep(3)
	sd.stop()
	return

def record():
	duration = 10.5  # seconds
	myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
	sd.wait()

def main():
	while True:
		try:
			number = int(input("Digite o numero:"))
			break
		except:
			print("Numero invalido")


	number = str(number)
	for i in range(len(number)):
		digit = number[i]
		sound_one = generateSin(number_table[digit][0],amplitude,t,fs)[1]
		sound_two = generateSin(number_table[digit][1], amplitude, t, fs)[1]
		sound = sound_one + sound_two
		play(sound)


if __name__ == '__main__':
	main()
	

