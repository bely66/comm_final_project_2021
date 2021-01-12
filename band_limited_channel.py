from utils import band_pass_filter, generate_square_signal
import matplotlib.pyplot as plt

## define time in secs and sampling freq
f_s = 1000
time = 10 

square_signal, t = generate_square_signal(time, f_s)


filtered_signal = band_pass_filter(cos_signal)
plt.figure(figsize=(10, 10))
plt.plot(square_signal, t)