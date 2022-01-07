'''Q001: Utilize uma estrutura de controle em um algoritmo que imprime a tabuada de 1 a 3.'''

num = 1
tabuada = 0
while num <= 3:
    while tabuada != 10:
        tabuada = tabuada + 1
        resultado = num * tabuada
        print(f"{num} X {tabuada} = {resultado}")
    tabuada = 0
    num = num + 1
