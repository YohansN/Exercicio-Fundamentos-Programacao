'''Q003: Gerar um vetor de 10 elementos. Em seguida, verifique quantos números primos existem no vetor, imprimindo-os.'''

from random import randint
lista_primos = []
con_primos = 0
vetor = []
for c in range(10):
  vetor.append(randint(0, 100))
print(vetor)
for c in range(10):
  if vetor[c] % 2 == 0 and vetor[c] % 1 == 0:
      pass
  else:
    con_primos += 1
    lista_primos.append(vetor[c])
print(f"A quantidade de números primos é {con_primos}. {lista_primos}")