%% Parte 1 - Faz a leitura das linhas (canais) 1 a 18 do arquivo .edf (EEG)
% no MATLAB
clear all
close all
clc
[hdr, record] = edfread(’nome_arquivo.edf’,’targetSignals’,1:18);

%% Parte 2 - Processamento do EEG e geração dos vetores de características
%
% Decomposição em 5 níveis do EEG utilizando as famílias Daubechies 4
% (db4), Coiflet 1 (coif1) e extração direta do sinal
%
% Tempo de 1 segundo (200 amostras por segundo) - Experimentos 1 e 2
%
tic; % inicia a contagem do tempo do processamento do script
clear all
close all
clc
%% carrega o sinal de EEG com a crise
A = load (’nome_arquivo.mat’);
A = A.nome_arquivo;
%% calcula o comprimento do sinal (quantidade de colunas) para ser
% utilizado no laço de repetição FOR
N = length(A)/200;
% pré-alocação dos vetores de características (processamento mais rápido)
vc_db = zeros(N,24);
vc_coif = zeros(N,24);
vc_sinal = zeros(N,4);
%%
for i = 1:N
% faz a varredura do sinal a cada 200 amostras (1 segundo)
A_trechos = A(:,(i-1)*200+1:i*200);
%% transforma a matriz EEG em um vetor linha
A_t = transpose(A_trechos);
B = reshape(A_t,1,[]);
%% cria os coeficientes cA5, cD5, cD4, cD3, cD2 e cD1 em C1 dos 5 níveis de
% decomposição e, nesta ordem, indica o comprimento de cada um deles em L1
% Família "db4"
[C1,L1] = wavedec(B,5,’db4’);
% extrai o coeficiente de aproximação cA5 de C
cA5_db = appcoef(C1,L1,’db4’,5);
% extrai os coeficientes de detalhe cD5, cD4, cD3, cD2 e cD1 de C
cD5_db = detcoef(C1, L1, 5);
cD4_db = detcoef(C1, L1, 4);
cD3_db = detcoef(C1, L1, 3);
cD2_db = detcoef(C1, L1, 2);
cD1_db = detcoef(C1, L1, 1);

%% cria os coeficientes cA5, cD5, cD4, cD3, cD2 e cD1 em C2 dos 5 níveis de
% decomposição e, nesta ordem, indica o comprimento de cada um deles em L2
% Família "coif1"
[C2,L2] = wavedec(B,5,’coif1’);
% extrai o coeficiente de aproximação cA5 de C
cA5_coif = appcoef(C2,L2,’coif1’,5);
% extrai os coeficientes de detalhe cD5, cD4, cD3, cD2 e cD1 de C
cD5_coif = detcoef(C2, L2, 5);
cD4_coif = detcoef(C2, L2, 4);
cD3_coif = detcoef(C2, L2, 3);
cD2_coif = detcoef(C2, L2, 2);
cD1_coif = detcoef(C2, L2, 1);

%% Vetor de Características - Família "db4"
% calcula a média, desvio padrão, valor máximo e valor mínimo para cada um
% dos 6 coeficientes gerados e cria o vetor de características
% para o treinamento e teste no SVM (24 características)
vc_db(i,:) = [mean(cA5_db) mean(cD5_db) mean(cD4_db) mean(cD3_db) ...
mean(cD2_db) mean(cD1_db) std(cA5_db) std(cD5_db) std(cD4_db) ...
std(cD3_db) std(cD2_db) std(cD1_db) max(cA5_db) max(cD5_db) max(cD4_db) ...
max(cD3_db) max(cD2_db) max(cD1_db) min(cA5_db) min(cD5_db) min(cD4_db) ...
min(cD3_db) min(cD2_db) min(cD1_db)];

%% Vetor de Características - Família "coif1"
% calcula a média, desvio padrão, valor máximo e valor mínimo para cada um
% dos 6 coeficientes gerados e cria o vetor de características
% para o treinamento e teste no SVM (24 características)
vc_coif(i,:) = [mean(cA5_coif) mean(cD5_coif) mean(cD4_coif) mean(cD3_coif) ...
mean(cD2_coif) mean(cD1_coif) std(cA5_coif) std(cD5_coif) std(cD4_coif) ...
std(cD3_coif) std(cD2_coif) std(cD1_coif) max(cA5_coif) max(cD5_coif) ...
max(cD4_coif) max(cD3_coif) max(cD2_coif) max(cD1_coif) min(cA5_coif) ...
min(cD5_coif) min(cD4_coif) min(cD3_coif) min(cD2_coif) min(cD1_coif)];

%% Vetor de Características - Extração direta do sinal
% calcula a média, desvio padrão, valor máximo, valor mínimo e energia
% da extração direta do sinal e cria o vetor de características
% para o treinamento e teste no SVM (5 características)
vc_sinal(i,:) = [mean(B(:)) std(B(:)) max(B(:)) min(B(:))];
end

toc; % finaliza a contagem do tempo do processamento do script