'''Q002: Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo: (2pt).
Nota Conceito
de 0,0 a 4,9 - D
de 5,0 a 6,9 - C
de 7,0 a 8,9 - B
de 9,0 a 10,0 - A'''

def nota_conceito(nota):
    if nota <= 4.9:
        print(f"Media final {nota} - D")
    elif 5 <= nota <= 6.9:
        print(f"Media final {nota} - C")
    elif 7 <= nota <= 8.9:
        print(f"Media final {nota} - B")
    elif 9 <= nota <= 10:
        print(f"Media final {nota} - A")
    else:
        print("Valor invalido")

nota = float(input("Media final: "))
nota_conceito(nota)