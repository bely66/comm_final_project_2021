# comm_final_project_2021

## Overview 
A signal is said to be band-limited or bandwidth-limited if it can be represented by a finite number of harmonics. Engineers limit the bandwidth of signals to enable multiple signals to share the same channel with minimal interference. A key result that pertains to bandwidth-limited signals is Nyquist’s sampling theorem, which states that a signal of bandwidth B can be reconstructed by taking 2B samples every second. In 1924, Harry Nyquist derived the following formula for the maximum data rate that can be achieved in a noiseless channel:
Maximum Data Rate = 2 B log2 V bits per second,
where B is the bandwidth of the channel and V is the number of discrete signal levels used in the channel. For example, to send only zeros and ones requires two signal levels. It is possible to envision any number of signal levels, but in practice the difference between signal levels must get smaller, for a fixed bandwidth, as the number of levels increases. And as the differences between signal levels decrease, the effect of noise in the channel becomes more pronounced.

Every channel has some sort of noise, which can be thought of as a random signal that contends with the message signal. If the noise is too great, it can obscure the message. Part of Shannon’s seminal contribution to information theory was showing how noise affects the message capacity of a channel. In particular, Shannon derived the following formula:
Maximum Data Rate = B log2(1 + S/N) bits per second,
where B is the bandwidth of the channel, and the quantity S/N is the signal-to-noise ratio, which is often given in decibels (dB). Observe that the larger the signal-to-noise ratio, the greater the data rate. Another point worth observing, though, is that the log2 function grows quite slowly. For example, suppose S/N is 1,000, then log2 1,001 = 9.97. If S/N is doubled to 2,000, then log2 2,001 = 10.97. Thus, doubling S/N produces only a 10 percent gain in the maximum data rate. Doubling S/N again would produce an even smaller percentage gain.


## Part 1
### Square Signal Before Channel 
![square pulse before channel time & freq](https://github.com/bely66/comm_final_project_2021/blob/master/square_before_channel.png)

### Square Signal After Channel 
![](https://github.com/bely66/comm_final_project_2021/blob/master/square_after_channel.png)

### Two square Pulses Before & After
![](https://github.com/bely66/comm_final_project_2021/blob/master/two_squares_before_after.png)

### Two Sinc Signals in time Before and After
![](https://github.com/bely66/comm_final_project_2021/blob/master/consecutive_sinc_before_after_time.png)

### Two Sinc Signals in Frequency
![](https://github.com/bely66/comm_final_project_2021/blob/master/consecutive_sinc_before_after_freq.png)
