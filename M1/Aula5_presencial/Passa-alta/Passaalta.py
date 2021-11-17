import numpy 
import matplotlib.pyplot as mp


vet_zeros = list(numpy.zeros(80)) #Cria lista de 0 
vet_coef = [] #Cria vetor para receber os coeficientes
filepath = "Coefs_PA_1k.dat"  #Abre o arquivo 
vet_entrada = list(numpy.memmap("sweep_100_3k4.pcm", dtype='h', mode='r')) #lê o sinal sonoro de entrada
vet_saida = [] #Cria vetor para a saída

with open(filepath,'r') as f: #Abre o arquivo e lê
    for line in f:
        vet_coef.append(line) #Armazena no vetor

    
for i in range(len(vet_entrada)): #Loop pelo vetor de entrada (sinal sonoro)
    x=0 # x = 0
    for j in range(len(vet_coef)): #For pelo vetor de coeficiente
        x = x + (float(vet_coef[j]) * float(vet_zeros[j])) #Multiplica e soma com o anterior
 
    vet_saida.append(x) #Armazena todo somatório na primeira posição 

    vet_zeros.pop(len(vet_zeros)-1) #Tira a última posição do vetor de zeros (amostras)
    vet_zeros.insert(0,vet_entrada[0]) #Insere a primeira posição do vetor de entrada
    vet_entrada.pop(0) #Tira a primeira posição do vetor de entrada



mp.plot(vet_saida) #Plota saída
mp.show()

with open('passa_alta.pcm', 'wb') as file: #Salva em PCM
    numpy.array(vet_saida, dtype=numpy.int16).tofile(file)
file.close()
