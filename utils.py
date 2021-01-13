from numpy import *
from numpy.fft import *

def blm_channel(length, fs, ch_bw):
    blm_freq=zeros(length))
    s=round(length/fs)*(fs/2-ch_bw))
    e=round(length/fs)*(fs/2+ch_bw))
    print(f"S {s}  e {e}")
    blm_freq[s:e] = 1
    return blm_freq

def square_pulse(length, start, end, on_value):
    square_pulse = zeros(length)
    square_pulse[start:end]=on_value

    return square_pulse

def signal_fft(in_signal):
    return fftshift(fft(in_signal))

def signal_real_ifft(in_signal):
    return real(fftshift(fft(in_signal)))



