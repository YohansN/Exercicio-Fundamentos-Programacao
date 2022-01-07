'''Q007: Escreva um algoritmo para ler um número inteiro e verifique se o número corresponde a um mês válido no calendário. Depois escrever o nome do mês, senão escrever uma mensagem “Mês Inválido”.'''

num = int(input())
if num > 0 and num <= 12:
    if num == 1:
        print("Janeiro")
    elif num == 2 :
        print("Fevereiro")
    elif num == 3 :
        print("Março")
    elif num == 4:
        print("Abril")
    elif num == 5:
        print("Maio")
    elif num == 6:
        print("Junho")
    elif num == 7:
        print("Julho")
    elif num == 8:
        print("Agosto")
    elif num == 9:
        print("Setembro")
    elif num == 10:
        print("Outubro")
    elif num == 11:
        print("Novembro")
    elif num == 12:
        print("Dezembro")
else:
    print("Mês invalido")

