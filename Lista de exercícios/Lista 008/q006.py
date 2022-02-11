'''Q006: Faça um programa em python para ler uma matriz em python 3 x 3, informado pelo usuário, que
represente uma turma de alunos com suas respectivas notas.
Cada linha deverá conter o nome do aluno e duas notas.
No final, o programa deverá emitir as seguintes informações:
a) Nome dos alunos com suas médias;
b) A maior e a menor média;'''

aluno1 = []
aluno2 = []
aluno3 = []
ordenador_media =[]

for i in range(0, 3):       #LINHA
    for j in range(0,3):    #COLUNA
        if j == 0:
            nome = str(input("Nome do aluno(a): "))
            if i == 0:
                aluno1.append(nome)
            elif i == 1:
                aluno2.append(nome)
            else:
                aluno3.append(nome)
        elif j == 1:
            n1 = float(input("Primeira Nota: "))
            if i == 0:
                aluno1.append(n1)
            elif i == 1:
                aluno2.append(n1)
            else:
                aluno3.append(n1)
        else:
            n2 = float(input("Segunda Nota: "))
            if i == 0:
                aluno1.append(n2)
            elif i == 1:
                aluno2.append(n2)
            else:
                aluno3.append(n2)

print("-="*25)
media1 = (aluno1[1] + aluno1[2]) / 2
ordenador_media.append(media1)
media2 = (aluno2[1] + aluno2[2]) / 2
ordenador_media.append(media2)
media3 = (aluno3[1] + aluno3[2]) / 2
ordenador_media.append(media3)
ordenador_media_crescente = sorted(ordenador_media)
print(f" Aluno(a): {aluno1[0]} - Média: {media1} \n Aluno(a): {aluno2[0]} - Média: {media2} \n Aluno(a): {aluno3[0]} - Média: {media3} \n")
print(f"Maior média: {ordenador_media_crescente[2]} - Menor média: {ordenador_media_crescente[0]}")