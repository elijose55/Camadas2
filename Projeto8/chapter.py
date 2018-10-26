
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import peakutils




class signalMeu:
    def __init__(self):
        self.init = 0

    def generateSin(self, freq, amplitude, time, fs):
        n = time*fs
        x = np.linspace(0.0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N  = len(signal)
        W = window.hamming(N)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))


    def plotFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        indexes = peakutils.indexes(y, thres = 0.2, min_dist = 30)

        plt.figure('Fourier')
        plt.plot(x, y)
        plt.xlim(0,2000)
        for i in range(len(x[indexes])):
            plt.plot(x[indexes][i],y[indexes][i],'ro')  

        # plt.xlim(round(x[indexes][0]-50),round(x[indexes][1] +300))
        # plt.ylim(-100, max(y[indexes])+2000 )
        plt.title('Fourier')
        plt.show()
        return x[indexes]


    def LowpassFilter(data,samplerate,cutoff_hz = 2000.0):
        nyq_rate = samplerate/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = signal.kaiserord(ripple_db, width)
        
        taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        yFiltrado = signal.lfilter(taps, 1.0, data)
        return yFiltrado

    def demodulate(self,signal, freq, fs, t):
        s, carrier = generateSin(freq,1,t,fs)
        demodulate = np.multiply(carrier,signal)

        return demodulate









