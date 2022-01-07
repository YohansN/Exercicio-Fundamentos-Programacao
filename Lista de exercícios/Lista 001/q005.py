'''Q005: Fazer um algoritmo para ler dois números inteiros e trocar seus valores; (ex.: A e B; valor de A passa para o B
e valor de B passa para o A); e depois imprimir os novos valores de cada variável.'''

A = int(input("A: "))
B = int(input("B: "))
aux = B 
B = A
A = aux
print(f"A: {A}")
print(f"B: {B}")
