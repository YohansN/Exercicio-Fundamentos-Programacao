'''Q005: Escreva um algoritmo para imprimir os números de 1 (inclusive) a 10 (inclusive) em ordem crescente,
e depois, em ordem decrescente.'''

print("Crescente:")
for i in range(1,11):
    print(i)
if i == 10:
    print("Decrescente:")
    for j in range(10, 0, -1):
        print(j)
print("fim")
