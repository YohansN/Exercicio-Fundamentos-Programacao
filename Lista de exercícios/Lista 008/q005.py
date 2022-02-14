'''Q005: Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Faça um programa em python que leia os nomes e os tempos (em segundos)
de cada volta de cada corredor e guarde as informações em uma matriz.
Ao final, o programa deve informar:
a) De quem foi a melhor volta da prova e em que volta;
b) Classificação final em ordem (1°. o campeão);
c) Qual foi a volta com a média mais rápida.'''

placar = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]

#Inputs na matriz Placar:
for i in range(0,6): #linha
    for j in range(0,11): #coluna
        if j == 0:
            placar[i][j] = str(input(f"Nome do {i + 1}° corredor: "))
        else:
            placar[i][j] = float(input(f"Tempo da {j}° volta em segundos: "))
    print("-="*50)

# a) De quem foi a melhor volta da prova e em que volta.
melhor_volta = 10000000
for i in range(0,6): #linha
    for j in range(1,11): #coluna
        if placar[i][j] < melhor_volta:
            piloto_melhor_volta = placar[i][0]
            melhor_volta = placar[i][j]
            numero_volta = j
print(f"– A melhor volta foi do piloto {piloto_melhor_volta}, com o tempo de {melhor_volta} segundos, feito na {numero_volta}° volta.\n")

# b) Classificação final em ordem (1°. o campeão).
tempo_piloto = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] #Matriz com o tempo e o nome do piloto para poder fazer o placar em ordem.
tempo_total = [[0],[0],[0],[0],[0],[0]] #O tempo total de cada piloto durante a corrida.
for i in range(0,6): #linha
    for j in range(1,11): #coluna
        tempo_total[i][0] += placar[i][j]
        tempo_piloto[i][0] += placar[i][j]
        tempo_piloto[i][1] = placar[i][0]

tempo_piloto = sorted(tempo_piloto)
tempo_total = sorted(tempo_total)
print("– Classificação final:")
for i in range(0,6):
    j = 1
    print(f"{i + 1}° Lugar – Piloto: {tempo_piloto[i][j]} – Tempo: {tempo_total[i]} segundos.")
    j += 2
print("\n")

# c) Qual foi a volta com a média mais rápida.
voltas = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],]
for i in range(0,6): #linha
    for j in range(1,11): #coluna            
        voltas[j-1][0] += placar[i][j]
media_volta = 10000000
for i in range(0, 10):
    if voltas[i][0] / 10 <= media_volta:     
        media_volta = voltas[i][0] / 10
        num_volta_mais_rapida = i + 1
print(f"– A volta de média mais rápida foi a {num_volta_mais_rapida}° volta, com tempo médio de {media_volta:.2f} segundos.\n")
