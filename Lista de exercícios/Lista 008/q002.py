'''Q002: Escreva uma função em python que, a partir de um vetor de cédulas [2, 5, 10, 20, 50, 100, 200],
seja capaz de calcular e informar a menor quantidade de cédulas em um determinado saque.
(P.ex.: “se a pessoa for sacar 250 reais, deverá obter 2 cédulas, uma de 200 e outra de 50”).'''

retirada = 0
cedulas = [2, 5, 10, 20, 50, 100, 200]

def retirar_cedulas():
    contador_notas = 0
    nota200 = 0
    nota100 = 0
    nota50 = 0
    nota20 = 0
    nota10 = 0
    nota5 = 0
    nota2 = 0
    reais = int(input("Digite o valor a ser retirado: "))
    print(f"Para sacar R${reais} foram retiradas: ")
    while reais != 0:
        if reais >= 200:
            retirada = cedulas[6]
            reais = reais - retirada
            nota200 = nota200 + 1 #Conta a quantidade retirada daquela cedula/nota.
            contador_notas += 1 #Conta a quantidade total retirada de cedulas/notas.
            
        elif 200 > reais >= 100:
            retirada = cedulas[5]
            reais -= retirada
            nota100 += 1
            contador_notas += 1
                
        elif 100 > reais >= 50:
            retirada = cedulas[4]
            reais -= retirada
            nota50 += 1
            contador_notas += 1
                
        elif 50 > reais >= 20:
            retirada = cedulas[3]
            reais -= retirada
            nota20 += 1
            contador_notas += 1
                
        elif 20 > reais >= 10:
            retirada = cedulas[2]
            reais -= retirada
            nota10 += 1
            contador_notas += 1
                
        elif 10 > reais >= 5:
            retirada = cedulas[1]
            reais -= retirada
            nota5 += 1
            contador_notas += 1
                
        elif 5 > reais >= 2:
            retirada = cedulas[0]
            reais -= retirada
            nota2 += 1
            contador_notas += 1
    
    while contador_notas != 0:
        if nota200 != 0:
            print(f"{nota200} Cedulas de R$200")
            nota200 = 0
        elif nota100 != 0:
            print(f"{nota100} Cedulas de R$100")
            nota100 = 0
        elif nota50 != 0:
            print(f"{nota50} Cedulas de R$50")
            nota50 = 0
        elif nota20 != 0:
            print(f"{nota20} Cedulas de R$20")
            nota20 = 0
        elif nota10 != 0:
            print(f"{nota10} Cedulas de R$10")
            nota10 = 0
        elif nota5 != 0:
            print(f"{nota5} Cedulas de R$5")
            nota5 = 0
        elif nota2 != 0:
            print(f"{nota2} Cedulas de R$2")
            nota2 = 0
        contador_notas -= 1
retirar_cedulas()