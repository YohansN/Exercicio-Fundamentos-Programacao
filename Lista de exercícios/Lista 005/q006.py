'''Q006: Gerar/Cria um vetor de 10 posições, randomicamente, depois ler um valor e verificar se esse valor está ou não no vetor gerado, mostrando a sua posição;'''

from random import randint
vetor = []
j = 0
for i in range(0, 10):
    vetor.append(randint(1, 100))
print(vetor)
num = int(input("Digite um valor: "))
if num in vetor:
    while j < 10:
        if num == vetor[j]:
            print(f"O valor está na {j}° posição da lista.")
            break
        else:
            j = j + 1
else:
    print("O valor digitado não se encontra na lista.")