'''Q004: Faça um programa em python que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma.
Imprima na tela a matriz, a linha de maior soma e a soma.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
matriz_soma = [[0],[0],[0]]
for i in range(0, 3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para a {i+1}° linha {j+1}° coluna: "))

maior_linha = sorted(matriz, reverse = True) #Coloca a linha com os maiores valores para o indice 0.

for i in range(0, 3):
    for j in range(0,3):
        matriz_soma[i][0] += matriz[i][j] #Soma as colunas.

matriz_soma = sorted(matriz_soma, reverse = True) 
maior_soma = matriz_soma[0] #Pega a linha de maior soma.

print(f" Matriz: {matriz} \n Linha de maior soma: {maior_linha[0]}\n Soma: {maior_soma}")