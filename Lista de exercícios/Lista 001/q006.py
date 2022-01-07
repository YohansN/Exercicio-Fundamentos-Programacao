'''Q006: Faça um algoritmo que calcule e imprima o An de uma P.A. (Progressão Aritmética), segundo a fórmula: An = a1 + (n-1) * r.'''

A1 = int(input("A1: "))
n = int(input("n: "))
r = int(input("r: "))
An = A1 + (n - 1) * r
print(f"An: {An}")
