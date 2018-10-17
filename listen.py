import sounddevice as sd
import numpy as np
import peakutils
from peakutils.plot import plot as pplot
import matplotlib.pyplot as plt
import time
from chapter import *
from sound import number_table

# %matplotlib inline

sinal = signalMeu()

duration = 2.0
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2
numbers = []

while len(numbers) == 0:
	print("Procurando por harmônicos...")
	recording = sd.rec(int(duration * fs), dtype = 'float64')
	recording = recording[:,0]
	sd.wait()



	# sd.play(recording,fs)
	# print(myrecording)
	# time.sleep(5.0)
	# sd.stop()
	# std = np.std()
	std = 25


	frequencies = sinal.plotFFT(recording,fs)
	print(frequencies)

	for e,i in number_table.items():
		for x in frequencies:
			if (i[0]-std <= x <= i[0] + std) and (i[1]-std <= x <= i[1] + std):
				print("é : ",e)
				numbers.append(e)
	if len(numbers) == 0:
		print("Nenhum harmônico encontrado, procurando de novo em 1 segundo.")
		time.sleep(1)




		



