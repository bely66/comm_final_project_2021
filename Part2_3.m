%%%%%%%%%%%%%% part 2 MultiPath %%%%%%%%%%%%%%
Energy_per_bit = 1;
SNR =[-15:0];
N = 1000;
X = randi([0 1],1,N);
BPSK = 2*(X)-1; 
H=MultipathChannel(N);
C=((H'*H)\eye(length(H),length(H)))*H'; %equation to get H' / const with th required array length
BER=zeros(1,length(SNR));
for i =1:1:length(SNR)
    No= Energy_per_bit/(10^(SNR(i)/10)); % 2 variance
    Noise=AWGN(BPSK,No); %calculate noise
    Y=H*transpose(BPSK)+transpose(Noise); %Y=HX+N
    EQ=real(C*Y); %equalized signal
    received_seq=decision(EQ); %convert signal to binary
    BER(i) = ComputeBER(X,received_seq); %calculate ber
end
display(BER);
f6=figure;
figure(f6);
plot(SNR,BER)
xlabel('SNR')
ylabel('BER')
grid on
%%
%%%%%% part 3 %%%%%%
%%%% Repetion channel coding %%% 
p_vect   = 0:0.1:0.5;           
total_bits = 1000; 
L=5;
r=1/L;
B_bits = randi([0,1],1,total_bits); 
C_bits = kron(B_bits,ones(1,L));
BER_vec  = zeros(size(p_vect)); 
for p_ind = 1:length(p_vect) 
    rx_data = zeros(size(C_bits)); 
    channel_effect = rand(size(rx_data))<=p_vect(p_ind);
    rx_data = xor(C_bits,channel_effect); 
   %uncoded bits and estimated bits are the same size
   %coded bits are same size with recieved coded bits
    Estimated_data_bits=zeros(1,length(B_bits));
    v=0;
    for i=1:(length(rx_data)/L)
            dh=0;  
            for c=1:L
                v=v+1;
                if rx_data(v)== 1
                    dh=dh+1; 
                end
            end
            if dh >=(L/2)  
                Estimated_data_bits(i)=1;
            elseif dh <=(L/2)
                Estimated_data_bits(i)=0;
            end
    end
   
BER_vec(p_ind) = ComputeBER(B_bits,Estimated_data_bits);
end
f7=figure;
figure(f7);
plot(p_vect,BER_vec,'g'); 
xlabel('Values of p')
ylabel('BER')


%%
%%%%%% part 3 %%%%%%
%%%% convolutional code %%% 
%GenerateBits
data = zeros(1,5);
data = round(rand(1,5))

%%%%%%%%%% convelutional encoder%%%%%%%%%
memory=[0 0 0];   % 3 encoder memory elements
encoded_sequence=zeros(1,(length(data))*2);
       
memory(1,3)=memory(1,2);
memory(1,2)=memory(1,1);
memory(1,1)=data(1,1);
temp=xor(memory(1),memory(2));      
X1=xor(temp,memory(3));             %generator polynomial=111 M1 XOR M2 XOR M3
X2=xor(memory(1),memory(3));        %generator polynomial=101 M1 XOR M3
encoded_sequence(1,1)=X1;             
encoded_sequence(1,2)=X2;             
data_len=length(data);
c=3;
for i=2:data_len
         
       memory(1,3)=memory(1,2);
       memory(1,2)=memory(1,1);
       if(i<=data_len)
       memory(1,1)=data(1,i);
       else
       memory(1,1)=0;
       end
              
       temp=xor(memory(1),memory(2));    
       X1=xor(temp,memory(3));
       X2=xor(memory(1),memory(3));
       
       encoded_sequence(1,c)=X1;    %x1 output encoded seq 
       c=c+1;
       encoded_sequence(1,c)=X2;    %x2 output encoded seq 
       c=c+1;
end
output_encoded_sequence=encoded_sequence

%%%%%%%%%%% Viterbi decoder%%%%%%%%%%%

trellis = poly2trellis(3,[7 5]);
tb = 4;
decoded_bits = vitdec(output_encoded_sequence,trellis,tb,'trunc','hard')