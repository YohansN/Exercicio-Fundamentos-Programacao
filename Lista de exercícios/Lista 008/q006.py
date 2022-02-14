'''Q006: Faça um programa em python para ler uma matriz em python 3 x 3, informado pelo usuário, que
represente uma turma de alunos com suas respectivas notas.
Cada linha deverá conter o nome do aluno e duas notas.
No final, o programa deverá emitir as seguintes informações:
a) Nome dos alunos com suas médias;
b) A maior e a menor média;'''

boletim = [[0,0,0],[0,0,0],[0,0,0]]
boletim_medias = [[0,0],[0,0],[0,0]]
medias = []
for i in range(0, 3):
    for j in range(0,3):
        if j == 0:
            boletim[i][j] = str(input("Nome do aluno(a): "))
            boletim_medias[i][0] = boletim[i][j]
        else:
            boletim[i][j] = float(input(f"{j}° Nota")) 

for i in range(0, 3):
    for j in range(1,3): #Percorre apenas as notas, somando-as.    
        boletim_medias[i][1] += boletim[i][j]
#print(boletim_medias)

for i in range(0, 3):
    for j in range(1,2):
        boletim_medias[i][1] = boletim_medias[i][1] / 2 #Faz a média das notas.
#print(boletim_medias)

for i in range(0,3):
    medias.append(boletim_medias[i][1])
    medias = sorted(medias)

print(f" Aluno(a): {boletim_medias[0][0]} - Média: {boletim_medias[0][1]:.2f} \n Aluno(a): {boletim_medias[1][0]} - Média: {boletim_medias[1][1]:.2f} \n Aluno(a): {boletim_medias[2][0]} - Média: {boletim_medias[2][1]:.2f} \n")
print(f"Maior média: {medias[2]:.2f} \n Menor média: {medias[0]:.2f}.")