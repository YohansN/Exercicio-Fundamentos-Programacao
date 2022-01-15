'''Q005: Preencher um vetor com os números 10 a 20, e depois mostrar os elementos pares do vetor de trás para frente.'''

vetor = []
par_invertido = []
j = 0
for i in range (10, 21):
    vetor.append(i)
while j != 11:
    if vetor[j] % 2 == 0:
        par_invertido.append(vetor[j])
        j = j + 1
    else:
        j = j + 1
par_invertido = sorted(par_invertido, reverse = True)
print(f"Vetor original: {vetor}")
print(f"Vetor apenas com elementos pares invertidos: {par_invertido}")