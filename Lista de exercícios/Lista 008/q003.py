'''Q003: Escreva uma função em python para calcular e informar o MDC (Máximo Divisor Comúm) de dois valores quaisquer informados pelo usuário.
P.ex: 24 e 36 - o MDC será 12'''

def calculador_mdc():
    div_primos = [2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    num1 = int(input("Digite o primeiro valor para o MDC: "))
    num1_inicial = num1
    num2 = int(input("Digite o segundo valor para o MDC: "))
    num2_inicial = num2
    
    mdc = 1
    i = 0
    while num1 != 1 and num2 != 1:
        if num1 % div_primos[i] == 0 and num2 % div_primos[i] == 0: #Divisão pelo qual os 2 números são divididos
            num1 = num1 / div_primos[i]
            num2 = num2 / div_primos[i]
            mdc = mdc * div_primos[i]
            if num1 % div_primos[i] != 0 and num2 % div_primos[i] != 0:
                i = i + 1
            
        elif num1 % div_primos[i] == 0 and num2 % div_primos[i] != 0: #Divisão pelo qual apenas o 1° número é dividido.
            num1 = num1 / div_primos[i]
            if num1 % div_primos[i] != 0 and num2 % div_primos[i] != 0:
                i = i + 1
            
        elif num1 % div_primos[i] != 0 and num2 % div_primos[i] == 0: #Divisão pelo qual apenas o 2° número é dividido.
            num2 = num2 / div_primos[i]
            if num1 % div_primos[i] != 0 and num2 % div_primos[i] != 0:
                i = i + 1
            
        elif num1 % div_primos[i] != 0 and num2 % div_primos[i] == 0: #Caso os dois números não sejam divisiveis pelos divisores.
            i += 1
            
    print(f"MDC ({num1_inicial}, {num2_inicial}) = {mdc}")

calculador_mdc()