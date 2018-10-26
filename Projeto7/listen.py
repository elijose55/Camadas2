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

duration = 3.0
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2
numbers = []

while len(numbers) == 0:
	print("Procurando por harmônicos...")
	recording = sd.rec(int(duration * fs), dtype = 'float64')
	sd.wait()
	recording = recording[:,0]


	plt.figure()
	# plt.xlim(0,500)
	# plt.ylim(-3,3)
	
	plt.plot(range(len(recording)),recording)
	plt.show()




	# sd.play(recording,fs)
	# print(myrecording)
	# time.sleep(5.0)
	# sd.stop()
	# std = np.std()
	std = 1


	peak_frequencies = sinal.plotFFT(recording,fs)
	print(peak_frequencies)

	for e,i in number_table.items():
		
			# print(i[0]-std,i[1]-std)
			# print("X : ",x)
		if (i[0]-std <= peak_frequencies[0] <= i[0] + std) and (i[1]-std <= peak_frequencies[1] <= i[1] + std):
			print("Numero : ",e)
			numbers.append(e)
	if len(numbers) == 0:
		print("Nenhum harmônico encontrado, procurando de novo em 1 segundo.")
		time.sleep(1)
	else:
		print("Harmonicos encontrados, encerrando.")
		break




		



