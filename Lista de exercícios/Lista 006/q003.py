'''Q003: Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada
linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.
Implemente uma matriz quadrada (quadrado mágico), insira valores aleatórios e, depois, mostre a
mensagem “É uma matriz QUADRADO MÁGICO” ou “NÃO é uma matriz QUADRADO MÁGICO” e os seus valores.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]] #matriz 3x3
for i in range(0, 3): #Número da coluna da matriz
    for j in range(0, 3): #Valores das linhas
        matriz[i][j] = int(input(f"Digite um valor para linha[{i}], coluna[{j}]"))
#8 somas do quadrado mágico:
#Horizontais:
a = matriz[0][0] + matriz[0][1] + matriz[0][2]
b = matriz[1][0] + matriz[1][1] + matriz[1][2]
c = matriz[2][0] + matriz[2][1] + matriz[2][2]
#Verticais:
d = matriz[0][0] + matriz[1][0] + matriz[2][0]
e = matriz[0][1] + matriz[1][1] + matriz[2][1]
f = matriz[0][2] + matriz[1][2] + matriz[2][2]
#Diagonais
g = matriz[0][0] + matriz[1][1] + matriz[2][2]
h = matriz[2][0] + matriz[1][1] + matriz[0][2]

print("--" *20)
if a == b == c == d == e == f == g == h:
    print("É uma matriz QUADRADO MÁGICO")
else:
    print("NÃO é uma matriz QUADRADO MÁGICO")
for i in range(0, 3):
    for j in range(0, 3):
        print(f"| {matriz[i][j]} |", end=' ')
    print("\n")