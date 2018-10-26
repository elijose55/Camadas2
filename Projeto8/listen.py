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
cutoff = 4000 #Hz
f_signal = 1200 #Hz
# f_carrier = 1000 #Hz

recording = sd.rec(int(duration * fs), dtype = 'float64')
sd.wait()
recording = recording[:,0]



demodulate = sinal.demodulate(recording,f_signal,fs,duration)
filtered = LowpassFilter(demodulate,fs,cutoff)


plt.plot(recording)
plt.show(block=False)
plt.pause(0.1)

sinal.plotFFT(filtered,fs)














		



