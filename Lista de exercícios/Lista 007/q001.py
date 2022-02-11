'''Q001: Apresente um programa em python que leia do teclado um caractere c e dois inteiros n1 e n2. Proceda da seguinte forma: (2pt).
Se o caractere for '+', calcule e imprima a soma n1 + n2.
Se o caractere for '-', calcule e imprima a subtração n1 - n2.
Se o caractere for '/', calcule e imprima a divisão n1/ n2.
Se o caractere for '*', calcule e imprima a multiplicação n1 * n2.
Caso contrário, exiba "Operação Inválida".'''

def calc(n1, n2):
    if c == "+":
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")
    elif c == "-":
        print(f"A subtração de {n1} por {n2} é {n1 - n2}")
    elif c == "/":
        print(f"A divisão de {n1} por {n2} é {n1 / n2}")
    elif c == "*":
        print(f"A mutiplicação de {n1} por {n2} é {n1 * n2}")
    else:
        print("Operação Inválida.")

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
c = str(input(" '+' para somar \n '-' para subtrair \n '/' para dividir \n '*' para multiplicar"))

calc(n1, n2)