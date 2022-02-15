'''Q001: Escreva uma função recursiva em python para mostrar a série fibonacci até o 12° termo.'''

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

for i in range(1, 13):
    print(f"{i}° termo - {fibonacci(i)}")