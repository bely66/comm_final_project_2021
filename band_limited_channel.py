from numpy import *
from numpy.fft import *

from utils import *

# Define the sampling freq
fs = 50e5
# The sampling time
Ts = 1/fs
# Number of samples
N =1e6
#Calculate the duration based on number of samples
time_domain= linspace(0,N/fs,int(N))

# Define the freq domain
frequency_domain=linspace(-fs/2,fs/2,len(time_domain))

# B = 100,000
channel_band_width=1e5
Tb=2/channel_band_width
Rb=1/Tb

# Make the band limited channel in frequency domain 
blm_freq = blm_channel(len(frequency_domain), fs, channel_band_width)

# Make square pulse in time domain
s=int((Tb*len(time_domain)/(N/fs)))
square_pulse_t1 = square_pulse(len(time_domain), 0, s, 1)

square_pulse_f1=signal_fft(square_pulse_t1)

square_pulse_rf1=square_pulse_f1*blm_freq

square_pulse_rt1=signal_real_ifft(square_pulse_rf1)


square_pulse_t2 = square_pulse(len(time_domain), s, 2*s, 1)
square_pulse_rf2 = signal_fft(square_pulse_t2)*blm_freq

square_pulse_rt2=signal_real_ifft(square_pulse_rf2)

s1=round((len(frequency_domain)/fs)*(fs/2-Rb/2))
e1=round((len(frequency_domain)/fs)*(fs/2+Rb/2))
sinc_pulse_f1 = square_pulse(len(frequency_domain), s1, e1, Tb)

sinc_pulse_t1=signal_real_ifft(sinc_pulse_f1)))

sinc_pulse_f2=exp(-2*pi*1j*Tb*frequency_domain)*sinc_pulse_f1
sinc_pulse_t2=signal_real_ifft(sinc_pulse_f2)))

sinc_pulse_rf1=sinc_pulse_f1*blm_freq
sinc_pulse_rt1=signal_real_ifft(sinc_pulse_rf1)))

sinc_pulse_rf2=sinc_pulse_f2*blm_freq
sinc_pulse_rt2=signal_real_ifft(sinc_pulse_rf2)))


from matplotlib.pyplot import *
# First Plot
figure(figsize=(20, 20))
subplot(2,1,1)
suptitle('signal before channel')
plot(time_domain[1:4*s],square_pulse_t1[1:4*s])
title('One square pulse in time domain')
xlabel('Time domain')
ylabel('Amplitude')
subplot(2,1,2)
plot(frequency_domain,real(square_pulse_f1))
xlim([-5*1e5, 5*1e5])
title('One square pulse in frequency domain')
xlabel('Frequency domain')
ylabel('Amplitude')
savefig("square_before_channel.png")

# Second Plot 

figure(figsize=(20, 20))
subplot(2,1,1)
suptitle('signal after channel')
plot(time_domain[1:4*s],square_pulse_rt1[1:4*s])
title('One square pulse in time domain')
xlabel('Time domain')
ylabel('Amplitude')
subplot(2,1,2)
plot(frequency_domain,real(square_pulse_rf1))
xlim([-5*1e5, 5*1e5])
title('One square pulse in frequency domain')
xlabel('Frequency domain')
ylabel('Amplitude')
savefig("square_after_channel.png")

# 3rd plot
figure(figsize=(20,20))
subplot(2,1,1)
suptitle('consecutive square pulse in time domain')
plot(time_domain[1:10*s],square_pulse_t1[1:10*s])
plot(time_domain[1:10*s],square_pulse_t2[1:10*s],'r')
title('before channel')
xlabel('Time domain')
ylabel('Amplitude')
xticks(rotation=90)
subplot(2,1,2)
plot(time_domain[1:10*s],square_pulse_rt1[1:10*s])
plot(time_domain[1:10*s],square_pulse_rt2[1:10*s],'r')
title('after channel')
xlabel('Time domain')
ylabel('Amplitude')
xticks(rotation=90)
savefig("two_squares_before_after.png")

# 4th plot 
figure(figsize=(20,20))
subplot(2,1,1)
suptitle('consecutive sinc in time domain')
plot(time_domain[1:10*s],fs*sinc_pulse_t1[1:10*s])
plot(time_domain[1:10*s],fs*sinc_pulse_t2[1:10*s],'r')
title('before channel')
xlabel('Time domain')
ylabel('Amplitude')
subplot(2,1,2)
plot(time_domain[1:10*s],fs*sinc_pulse_rt1[1:10*s])
plot(time_domain[1:10*s],fs*sinc_pulse_rt2[1:10*s],'r')
title('after channel')
xlabel('Time domain')
ylabel('Amplitude')
savefig("consecutive_sinc_before_after_time.png")

#5th plot 
figure(figsize=(20,20))
subplot(2,1,1)
suptitle('consecutive sinc in frequency domain')
plot(frequency_domain,abs(sinc_pulse_f1))
xlim([-5*1e5, 5*1e5])
plot(frequency_domain,abs(sinc_pulse_f2))
xlim([-5*1e5, 5*1e5])
title('before channel')
xlabel('Frequency domain')
ylabel('Amplitude')
subplot(2,1,2)
plot(frequency_domain,abs(sinc_pulse_rf1))
xlim([-5*1e5, 5*1e5])
plot(frequency_domain,abs(sinc_pulse_rf2))
xlim([-5*1e5, 5*1e5])
title('after channel')
xlabel('Frequency domain')
ylabel('Amplitude')
savefig("consecutive_sinc_before_after_freq.png")




