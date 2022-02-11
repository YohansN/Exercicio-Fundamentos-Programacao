'''Q003: Crie uma função em python que receba 3 números e retorne em forma crescente.'''

def ordem_crescente(a, b, c):
    print("Ordem crescente:")
    if a > b > c or a == b > c or a > b == c:
        print(c, b, a)
    elif a > c > b or a == c > b or a > c == b:
        print(b, c, a)
    elif b > a > c or b == a > c or b > a == c:
        print(c, a, b)
    elif b > c > a or b == c > a or b > c == a:
        print(a, c, b)
    elif c > a > b or c == a > b or c > a == b:
        print(b, a, c)
    elif c > b > a or c == b > a or c > b == a:
        print(a, b, c)
    elif a == b == c:
        print(a, b, c)
    
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
ordem_crescente(a, b, c)

