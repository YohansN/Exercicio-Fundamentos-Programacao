'''Q004: Crie um algoritmo que leia 3 números e imprima o maior valor.'''

A, B, C = input("Valores para A, B, C: ").split()
if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
elif C > A and C > B:
    print(C)
