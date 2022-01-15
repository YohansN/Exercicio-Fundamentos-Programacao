'''Q004: Crie um vetor de inteiros para armazenar a sequência Fibonacci até a 20a. posição.'''

vetor = []
def fib(n):
    if n <= 0:
        return 0
    elif n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
for i in range(21):
    vetor.append(fib(i))
print(vetor)
