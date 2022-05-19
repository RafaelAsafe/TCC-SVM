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
%% utilizado no laço de repetição FOR
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
%% decomposição e, nesta ordem, indica o comprimento de cada um deles em L2
%% Família "coif1"
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

%% Parte 3 - Normalização (escalonamento) dos vetores de características e
% utilização da Máquina de Vetores de Suporte (SVM) através do pacote LibSVM
% Exoerimentos 1 e 2
tic; % inicia a contagem do tempo do processamento do script
clear all
close all
clc

%% carrega o vetor de características e as classes referente a cada linha
load vc_sinal_ce; % carrega os dados de CE
load vc_sinal_ce_label; % carrega as classes dos dados de CE
load vc_sinal_cnep; % carrega os dados de CNEP
load vc_sinal_cnep_label; % carrega as classes dos dados de CNEP
v = vc_sinal_ce(:,1:4);
vc_n_ce_label = vc_sinal_ce_label;
w = vc_sinal_cnep(:,1:4);
vc_n_cnep_label = vc_sinal_cnep_label;

%% faz a normalização (escalonamento) dos vetores de características de
% crises epilépticas (ce) no intervalo entre [-1 e 1]
a = max (v(:));
b = min (v(:));
vx = 2* v / (a-b);
c = min (vx(:));
%SVM - janelas de 1 segundo das crises - Experimentos 1 e 2 123
vc_n_ce = vx - (c + 1); % vetor normalizado de treinamento

%% faz a normalização (escalonamento) dos vetores de características de
% crises não epilépticas psicogênicas (cnep) no intervalo entre [-1 e 1]
c = max (w(:));
d = min (w(:));
wx = 2* w / (c-d);
d = min (wx(:));
vc_n_cnep = wx - (d + 1); % vetor normalizado de avaliação

%% seleciona um dos Itens para treinamento e avaliação


sel_caso = 9;
switch(sel_caso)
% faz a leitura dos dados de treinamento e avaliação (Item 1)
% Treinamento CE: pacientes 12 a 29, Avaliação CE: pacientes 30, 10 a 11
% Treinamento CNEP: pacientes 1 a 9, Avaliação CNEP: pacientes 10 a 11
case 1
train_data = [vc_n_ce(1:6104,:);vc_n_cnep(1:2111,:)];
train_label = [vc_n_ce_label(1:6104,:);vc_n_cnep_label(1:2111,:)];
test_data = [vc_n_ce(6105:6778,:);vc_n_cnep(2112:2717,:)];
test_label = [vc_n_ce_label(6105:6778,:);vc_n_cnep_label(2112:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 2)
% Treinamento CE: pacientes 12 a 27, Avaliação CE: pacientes 28 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1 a 8, Avaliação CNEP: pacientes 9 a 11
case 2
train_data = [vc_n_ce(1:5783,:);vc_n_cnep(1:2058,:)];
train_label = [vc_n_ce_label(1:5783,:);vc_n_cnep_label(1:2058,:)];
test_data = [vc_n_ce(5784:6778,:);vc_n_cnep(2059:2717,:)];
test_label = [vc_n_ce_label(5784:6778,:);vc_n_cnep_label(2059:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 3)
% Treinamento CE: pacientes 12 a 25, Avaliação CE: pacientes 26 a 30, 10 a
SVM - janelas de 1 segundo das crises - Experimentos 1 e 2 124
% 11
% Treinamento CNEP: pacientes 1 a 7, Avaliação CNEP: pacientes 8 a 11
case 3
train_data = [vc_n_ce(1:5483,:);vc_n_cnep(1:2004,:)];
train_label = [vc_n_ce_label(1:5483,:);vc_n_cnep_label(1:2004,:)];
test_data = [vc_n_ce(5484:6778,:);vc_n_cnep(2005:2717,:)];
test_label = [vc_n_ce_label(5484:6778,:);vc_n_cnep_label(2005:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 4)
% Treinamento CE: pacientes 12 a 23, Avaliação CE: pacientes 24 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1 a 6, Avaliação CNEP: pacientes 7 a 11
case 4
train_data = [vc_n_ce(1:5423,:);vc_n_cnep(1:1919,:)];
train_label = [vc_n_ce_label(1:5423,:);vc_n_cnep_label(1:1919,:)];
test_data = [vc_n_ce(5424:6778,:);vc_n_cnep(1920:2717,:)];
test_label = [vc_n_ce_label(5424:6778,:);vc_n_cnep_label(1920:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 5)
% Treinamento CE: pacientes 12 a 21, Avaliação CE: pacientes 22 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1 a 5, Avaliação CNEP: pacientes 6 a 11
case 5
train_data = [vc_n_ce(1:4868,:);vc_n_cnep(1:1819,:)];
train_label = [vc_n_ce_label(1:4868,:);vc_n_cnep_label(1:1819,:)];
test_data = [vc_n_ce(4869:6778,:);vc_n_cnep(1820:2717,:)];
test_label = [vc_n_ce_label(4869:6778,:);vc_n_cnep_label(1820:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 6)
% Treinamento CE: pacientes 12 a 19, Avaliação CE: pacientes 20 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1 a 4, Avaliação CNEP: pacientes 5 a 11
case 6
train_data = [vc_n_ce(1:4550,:);vc_n_cnep(1:1459,:)];
train_label = [vc_n_ce_label(1:4550,:);vc_n_cnep_label(1:1459,:)];
test_data = [vc_n_ce(4551:6778,:);vc_n_cnep(1460:2717,:)];
test_label = [vc_n_ce_label(4551:6778,:);vc_n_cnep_label(1460:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 7)
% Treinamento CE: pacientes 12 a 17, Avaliação CE: pacientes 18 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1 a 3, Avaliação CNEP: pacientes 4 a 11
case 7
train_data = [vc_n_ce(1:4326,:);vc_n_cnep(1:1004,:)];
train_label = [vc_n_ce_label(1:4326,:);vc_n_cnep_label(1:1004,:)];
test_data = [vc_n_ce(4327:6778,:);vc_n_cnep(1005:2717,:)];
test_label = [vc_n_ce_label(4327:6778,:);vc_n_cnep_label(1005:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 8)
% Treinamento CE: pacientes 12 a 15, Avaliação CE: pacientes 16 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1 a 2, Avaliação CNEP: pacientes 3 a 11
case 8
train_data = [vc_n_ce(1:3175,:);vc_n_cnep(1:263,:)];
train_label = [vc_n_ce_label(1:3175,:);vc_n_cnep_label(1:263,:)];
test_data = [vc_n_ce(3176:6778,:);vc_n_cnep(264:2717,:)];
test_label = [vc_n_ce_label(3176:6778,:);vc_n_cnep_label(264:2717,:)];
% faz a leitura dos dados de treinamento e avaliação (Item 9)
% Treinamento CE: pacientes 12 a 13, Avaliação CE: pacientes 14 a 30, 10 a
% 11
% Treinamento CNEP: pacientes 1, Avaliação CNEP: pacientes 2 a 11
case 9
train_data = [vc_n_ce(1:1550,:);vc_n_cnep(1:139,:)];
train_label = [vc_n_ce_label(1:1550,:);vc_n_cnep_label(1:139,:)];
test_data = [vc_n_ce(1551:6778,:);vc_n_cnep(140:2717,:)];
test_label = [vc_n_ce_label(1551:6778,:);vc_n_cnep_label(140:2717,:)];
end

%% faz o treinamento na SVM - Kernel "Linear"
model_L = svmtrain(train_label, train_data, ’-b 1 -h 0 -t 0’);
% faz a previsão na SVM
[predict_label_L, accuracy_L, prob_estimates_L] = ...
svmpredict(test_label, test_data, model_L, ’-b 1’);

% gera a matriz de confusão e calcula a Acurácia, Sensitividade e
% Especificidade
[cMatrix_L,cOrder_L] = confusionmat(test_label,predict_label_L);
sensitivity_L = 100*(cMatrix_L(2,2)/(sum(cMatrix_L(2,:))));
specificity_L = 100*(cMatrix_L(1,1)/(sum(cMatrix_L(1,:))));
result_L = [accuracy_L(1,1) sensitivity_L specificity_L];
display(result_L’);

%% faz o treinamento na SVM - Kernel "Polinomial"
model_P = svmtrain(train_label, train_data, ’-b 1 -h 0 -t 1’);
% faz a previsão na SVM
[predict_label_P, accuracy_P, prob_estimates_P] = ...
svmpredict(test_label, test_data, model_P, ’-b 1’);
% gera a matriz de confusão e calcula a Acurácia, Sensitividade e
% Especificidade
[cMatrix_P,cOrder_P] = confusionmat(test_label,predict_label_P);
sensitivity_P = 100*(cMatrix_P(2,2)/(sum(cMatrix_P(2,:))));
specificity_P = 100*(cMatrix_P(1,1)/(sum(cMatrix_P(1,:))));
result_P = [accuracy_P(1,1) sensitivity_P specificity_P];
display(result_P’);

%% faz o treinamento na SVM - Kernel "RBF"
model_R = svmtrain(train_label, train_data, ’-b 1 -h 0 -t 2’);
% faz a previsão na SVM
[predict_label_R, accuracy_R, prob_estimates_R] = ...
svmpredict(test_label, test_data, model_R, ’-b 1’);
% gera a matriz de confusão e calcula a Acurácia, Sensitividade e
% Especificidade
[cMatrix_R,cOrder_R] = confusionmat(test_label,predict_label_R);
sensitivity_R = 100*(cMatrix_R(2,2)/(sum(cMatrix_R(2,:))));
specificity_R = 100*(cMatrix_R(1,1)/(sum(cMatrix_R(1,:))));
result_R = [accuracy_R(1,1) sensitivity_R specificity_R];
display(result_R’);

%% faz o treinamento na SVM - Kernel "Sigmoide"
model_S = svmtrain(train_label, train_data, ’-b 1 -h 0 -t 3’);
% faz a previsão na SVM
[predict_label_S, accuracy_S, prob_estimates_S] = ...
svmpredict(test_label, test_data, model_S, ’-b 1’);
% gera a matriz de confusão e calcula a Acurácia, Sensitividade e
% Especificidade
[cMatrix_S,cOrder_S] = confusionmat(test_label,predict_label_S);
sensitivity_S = 100*(cMatrix_S(2,2)/(sum(cMatrix_S(2,:))));
specificity_S = 100*(cMatrix_S(1,1)/(sum(cMatrix_S(1,:))));
result_S = [accuracy_S(1,1) sensitivity_S specificity_S];
display(result_S’);
toc; % finaliza a contagem do tempo do processamento do script