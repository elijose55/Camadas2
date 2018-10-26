import numpy as np
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import signal as window
from scipy.fftpack import fft

def generateSin(freq, amplitude, time, fs):
    n = time*fs
    x = np.linspace(0.0, time, n)
    s = amplitude*np.sin(freq*x*2*np.pi)
    return (x, s)




def normalizeSignal(data):
    data_max = max(data)
    #print(data_max)
    data_min = min(data)
    #print(data_min)
    normalized_data = []
    for i in range(len(data)):
        normalized_data.append((data[i]-data_min)/(data_max-data_min))

    return normalized_data


def filter(data, samplerate):
	#exemplo de filtragem do sinal yAudioNormalizado
	# https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
	nyq_rate = samplerate/2
	width = 5.0/nyq_rate
	ripple_db = 60.0 #dB
	N , beta = signal.kaiserord(ripple_db, width)
	cutoff_hz = 5000
	taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
	filtered_data = signal.lfilter(taps, 1.0, data)

	return filtered_data

def calcFFT(signal, fs):
    # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
    N  = len(signal)
    W = window.hamming(N)
    T  = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal*W)
    return(xf, np.abs(yf[0:N//2]))


def plotFFT(signal, fs):
    x,y = calcFFT(signal, fs)
    plt.figure()
    plt.plot(x, np.abs(y))
    plt.title('Fourier')



freq = 14000
amplitude = 1
fs = 44100

data, samplerate = sf.read('voz.wav')

amplitude_vector = data[:,0]
tempo = len(amplitude_vector)/fs
#print(len(amplitude_vector))

normalized_data = normalizeSignal(amplitude_vector)

filtered_data = filter(normalized_data, fs)

x, s = generateSin(freq, amplitude, tempo, fs)
modulated_data = np.multiply(filtered_data,s)

#print(filtered_data)
sd.play(modulated_data,fs)
sd.wait()

#tempo = np.linspace(0, tempo*fs, tempo*fs)
tempo = np.linspace(0,tempo,len(amplitude_vector))
print(filtered_data)

print(modulated_data)


plt.plot(tempo, amplitude_vector)
plt.title("Initial Signal")
plotFFT(amplitude_vector, fs)
plt.show()

plt.plot(tempo, normalized_data)
plt.title("Normalized data")
plotFFT(normalized_data, fs)
plt.show()
plt.plot(tempo, filtered_data)
plt.title("Filtered signal")
plotFFT(filtered_data, fs)
plt.show()

plt.plot(tempo,modulated_data)
plt.title("Modulated data")
plotFFT(modulated_data, fs)
plt.show()


