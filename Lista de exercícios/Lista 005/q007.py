'''Q007: Gerar/Cria um vetor de 10 posições, randomicamente, depois contar quantos pares e quantos ímpares existem no vetor;'''

from random import randint
vetor = []
par = []
impar = []
contador_par = 0
contador_impar = 0
for i in range(0, 10):
    vetor.append(randint(0, 100))
j = 0
while j < 10:
    if vetor[j] % 2 == 0:
        par.append(vetor[j])
        contador_par = contador_par + 1
    else:
        impar.append(vetor[j])
        contador_impar = contador_impar + 1
    j = j + 1
print(f"Vetor original: {vetor}")
print(f"Os {contador_par} números pares do vetor são: {par}")
print(f"Os {contador_impar} números ímpares do vetor são: {impar}")