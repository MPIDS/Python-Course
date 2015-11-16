clear all;
%% create data
%rng(42);
N=1e4;
epsilon=.2;
n=20;
t=(0:N-1)'/(N-1);
signal(:,1)=sin(2*pi*t*n)+epsilon*randn(N,1);
signal(:,2)=sin(2*pi*t*n).*cos(2*pi*t*n*.1)+epsilon*randn(N,1);

%% data 1 (matrix)
save('data.mat','signal','t')

%% data 2 (struct)
data=[];
data.t=t;
data.signal=signal;
save('data1.mat','data')

%% data 3 (cell)
clear data;
data{1}=t;
data{2}=signal.*[sin(2*pi*t*2),sin(2*pi*t*2)];
save('data2.mat','data')
