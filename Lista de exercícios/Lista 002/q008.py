'''Q008: Faça um algoritmo que recebe a média final de um aluno e imprima o seu conceito, conforme a tabela abaixo:
Média Conceito
de 0,0 a 4,9 - D
de 5,0 a 6,9 - C
de 7,0 a 8,9 - B
de 9,0 a 10,0 - A'''

Media_Final = float(input("Media Final: "))
if Media_Final >= 0 and Media_Final <= 4.9:
    print("D")
elif Media_Final >= 5 and Media_Final <= 6.9:
    print("C")
elif Media_Final >= 7 and Media_Final <= 8.9:
    print("B")
elif Media_Final >= 9 and Media_Final <= 10:
    print("A")
