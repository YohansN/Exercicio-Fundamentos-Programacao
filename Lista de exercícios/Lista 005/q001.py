'''Q001: Gerar um vetor aleatório de 10 posições, em seguida ordená-lo de forma crescente e, depois, decrescente.'''

from random import randint
vetor = []
for i in range(0, 10):
    vetor.append(randint(0, 100))
print(f"Vetor originalmente gerado: {vetor}")
print(f"Vetor ordenado de forma crescente: {sorted(vetor)}")
print(f"Vetor ordenado de forma decrescente: {sorted(vetor, reverse = True)}")
