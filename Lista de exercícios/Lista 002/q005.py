'''Q005: Escrever um algoritmo para ler dois valores numéricos e apresentar a diferença do maior pelo menor.'''

A = int(input("Valor para A: "))
B = int(input("Valor para B: "))
if A > B:
    print(A - B)
else:
    print(B - A)
