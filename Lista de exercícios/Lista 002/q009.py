'''Q009: Faça um algoritmo que leia do teclado um caractere c e dois inteiros n1 e n2. Proceda da seguinte forma
utilizando uma estrutura de controle:
- Se o caractere for '+', calcule e imprima a soma n1 + n2.
- Se o caractere for '-', calcule e imprima a subtração n1 - n2.
- Se o caractere for '/', calcule e imprima a divisão n1/ n2.
- Se o caractere for '*', calcule e imprima a multiplicação n1 * n2.
- Caso contrário, exiba "Operação Inválida".'''

c = str(input("Caracter: '+' '-' '/' '*': "))
n1 = int(input("Digite 1 valor: "))
n2 = int(input("Digite mais 1 valor: "))
if c == "+":
    resultado = n1 + n2
    print(resultado)
elif c == "-":
    resultado = n1 - n2
    print(resultado)
elif c == "/":
    resultado = n1 / n2
    print(resultado)
elif c == "*":
    resultado = n1 * n2
    print(resultado)
else:
    print("Operação Inválida")
