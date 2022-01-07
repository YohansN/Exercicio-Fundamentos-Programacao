'''Q007: Faça um algoritmo para calcular e imprimir o An de uma P.G. (Progressão Geométrica), segundo a formula: An = A1*q^n-1.'''

A1 = int(input("A1: "))
q = int(input("q: "))
n = int(input("n: "))
An = A1 * (q**(n - 1))
print(f"An: {An}")
