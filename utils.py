import numpy as np
from scipy import signal
from scipy.fftpack import rfft, irfft, fftfreq
from scipy.signal import butter, lfilter

def pulse_shaping():
    pass


def generate_cos_signal(freq, time, sampling_frequency):
    nsamples = time * sampling_frequency
    time   = np.linspace(0, time, nsamples)
    cos_signal = np.cos(freq*2*np.pi*time) 
    return cos_signal, time
def generate_square_signal(time, sampling_frequency):
    nsamples = int(time * sampling_frequency)
    time_range   = np.linspace(0, time, nsamples)
    factor = (2*np.pi)/time
    square_signal = signal.square(factor*time_range, 1)
    return square_signal, time_range


def compute_BER(input_sig, output_signal):
    pass

def awgn_channel():
    pass


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y