'''Q003: Faça um algoritmo que leia um valor inteiro e verifica se o valor é par ou ímpar, retornando um valor booleano.'''

num = int(input())
x = num % 2
if x == 1:
    impar = True
    par = False
    print(f"Par: {par}")
    print(f"Ímpar: {impar}")
elif x == 0:
    impar = False
    par = True
    print(f"Par: {par}")
    print(f"Ímpar: {impar}")

