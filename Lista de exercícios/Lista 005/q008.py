'''Q008: Gerar/Cria um vetor de 10 posições, randomicamente, depois contar quantos valores repetidos existem no vetor gerado, imprimindo-os se houver;'''

from random import randint
vetor = []
for i in range(0, 10):
    vetor.append(randint(0, 10))
print(f"Vetor original: {vetor}")
repete = 0
repetidos = []
for j in vetor:
    for k in vetor:
        if j == k:
            repete = repete + 1
            if repete == 2:
                if k in repetidos:
                    pass
                else:
                    repetidos.append(k)
            else:
                pass
        else:
            pass
    repete = 0
print(f"Valores repetidos: {repetidos}")