'''Q004: Faça um programa em python que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma.
Imprima na tela a matriz, a linha de maior soma e a soma.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
ordenador = []
linha1 = []
linha2 = []
linha3 = []
somal1 = 0
somal2 = 0
somal3 = 0

for i in range(0, 3):       #LINHA
    for j in range(0,3):    #COLUNA
        matriz[i][j] = int(input(f"Digite um valor para a {i+1}° linha {j+1}° coluna: "))
        if i == 0:
            somal1 += matriz[i][j]
            linha1.append(matriz[i][j])
        elif i == 1:
            somal2 += matriz[i][j]
            linha2.append(matriz[i][j])
        elif i == 2:
            somal3 += matriz[i][j]
            linha3.append(matriz[i][j])

#Maior soma:
if sum(linha1) >= sum(linha2) > sum(linha3):
    maior_soma = sum(linha1)
    linha_maior_soma = linha1
elif sum(linha1) >= sum(linha3) > sum(linha2):
    maior_soma = sum(linha1)
    linha_maior_soma = linha1
elif sum(linha2) >= sum(linha1) > sum(linha3):
    maior_soma = sum(linha2)
    linha_maior_soma = linha2
elif sum(linha2) >= sum(linha3) > sum(linha1):
    maior_soma = sum(linha2)
    linha_maior_soma = linha2
elif sum(linha3) >= sum(linha1) > sum(linha2):
    maior_soma = sum(linha3)
    linha_maior_soma = linha3
elif sum(linha3) >= sum(linha2) > sum(linha1):
    maior_soma = sum(linha3)
    linha_maior_soma = linha3
else:
    linha_maior_soma = "Empate"
    maior_soma = "Empate"

print(f" Matriz: {matriz} \n Linha de maior soma: {linha_maior_soma}\n Soma: {maior_soma}")
