
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
        indexes = peakutils.indexes(y, thres = 0.5, min_dist = 30)

        plt.figure('Fourier')
        plt.plot(x, y)
        for i in range(len(x[indexes])):
            plt.plot(x[indexes][i],y[indexes][i],'ro')  

        # plt.xlim(round(x[indexes][0]-50),round(x[indexes][1] +300))
        # plt.ylim(-100, max(y[indexes])+2000 )
        plt.title('Fourier')
        plt.show(block=False)
        return y[indexes]

