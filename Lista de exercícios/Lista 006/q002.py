'''Q002: Deseja-se fazer a emissão da folha de pagamento de uma empresa.
Para os 4 funcionários de uma empresa são dadas as seguintes informações: (matrícula, nome, função e salário).
Implemente uma matriz 4 x 4 para emissão dessas informações, depois mostre quem ganha o maior e o menor salário.'''

maior_salario = 0
menor_salario = 1000000000000
nome_maior_salario = ''
nome_menor_salario = ''
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],]
for i in range(0, 4): #Numero da coluna da matriz (0, 1, 2, 3)
    for j in range(0, 4): #Valores (0:matricula; 1:nome; 2:funcao; 3:salario)
        if j == 0:
            matriz[i][j] = int(input(f"{i+1}° Matrícula: "))
        elif j == 1:
            nome = str(input(f"{i+1}° Nome: "))
            matriz[i][j] = nome
        elif j == 2:
            matriz[i][j] = str(input(f"{i+1}° Função: "))
        elif j == 3:
            salario = int(input(f"{i+1}° Salário: "))
            matriz[i][j] = salario
            if salario >= maior_salario:
                maior_salario = salario
                nome_maior_salario = nome
            if salario < menor_salario:
                menor_salario = salario
                nome_menor_salario = nome
print("-="*30)
print("Matrícula - Nome - Função - Salário")
print(matriz)
print("-="*30)
print(f"O valor do maior salário é R$ {maior_salario}, do funcionário: {nome_maior_salario}")
print(f"O valor do menor salário é R$ {menor_salario}, do funcionário: {nome_menor_salario}")
