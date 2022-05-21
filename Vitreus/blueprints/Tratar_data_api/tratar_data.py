# preciso converter em uma rest api
import mne
import pandas as pd

mne.utils.set_config('MNE_USE_CUDA', 'false')

path = "C:\\Users\\Mysterio\\OneDrive - ifsp.edu.br\\Documentos\\Asafe IFSP\\TCC\\programação\\MLmodel\\Patients_data\\Patients\\PNES\\Patient 1\\1-evento_10_57.edf"
file = 'event1_patient1.csv' # alterar para pegar o nome automaticamente do arquivo
raw_data = mne.io.read_raw_edf(path, preload=True).load_data()

raw_data.pick_channels([ 'EEG Fp1-Ref',
 'EEG Fp2-Ref',
 'EEG F3-Ref',
 'EEG F4-Ref',
 'EEG C3-Ref',
 'EEG C4-Ref',
 'EEG P3-Ref',
 'EEG P4-Ref',
 'EEG O1-Ref',
 'EEG O2-Ref',
 'EEG F7-Ref',
 'EEG F8-Ref',
 'EEG T7-Ref',
 'EEG T8-Ref',
 'EEG P7-Ref',
 'EEG P8-Ref',
 'EEG Fz-Ref',
 'EEG Cz-Ref',
 'EEG Pz-Ref'])

low_freq, high_freq = 0.3, 30.0
raw_data = raw_data.filter(low_freq, high_freq,n_jobs=4)

data = raw_data.to_data_frame()
data.index+=1# configurando o index para começar do 1(se reproduzir isso novamente vai cagar no bagulho kkkkkk)
data.round(decimals=2) # arredondando o numero de casa decimais para 2

data.to_excel(file +'.xlsx')
