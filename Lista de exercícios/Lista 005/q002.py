'''Q002: Preencher um primeiro vetor com o quadrado dos números pares do intervalo 2 a 20.
Preencher um segundo vetor com os números de 10 a 19.Mostrar a soma dos dois vetores.'''

vetor1 = []
vetor2 = []
vetor_soma = []
for i in range(2, 21):
    if i % 2 == 0:
        vetor1.append(i**2)
for j in range(10, 20):
    vetor2.append(j)
print(f"Quadrado dos números pares do intervalo 2 a 20: {vetor1}")
print(f"Números de 10 a 19: {vetor2}")
k = 0
while k < 10:
    num = vetor1[k] + vetor2[k]
    vetor_soma.append(num)
    k = k + 1
print(f"Soma dos dois vetores: {vetor_soma}")