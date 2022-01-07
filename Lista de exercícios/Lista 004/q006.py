'''Q006: A prefeitura de uma cidade deseja fazer uma pesquisa para coletar dados sobre o salário e número
de filhos de cada habitante. Faça um algoritmo para ler os dados de 5 habitantes e escrever: a) Média
de salário da população; b) Média do número de filhos; c) Percentual de pessoas com salário menor
que R$ 1000,00.'''

salario_baixo = 0
total_salario = 0
total_filhos = 0
entrevistados = 0
for i in range(1, 6):
    print(f"{i}º entrevistado:" )
    salario = float(input("Quanto é seu salário? "))
    if salario < 1000:
        salario_baixo = salario_baixo + 1
    total_salario = total_salario + salario
    filhos = int(input("Quantos filhos você tem? "))
    total_filhos = total_filhos + filhos
    entrevistados = entrevistados + 1
    print("------------------------------")
med_salario = total_salario / 5
med_filhos = total_filhos / 5
perc_salario = (salario_baixo / entrevistados)* 100 #Pessoas com salário abaixo de 1000.

print(f"a) Média de salário da população: {med_salario}")
print(f"b) Média do número de filhos: {med_filhos}")
print(f"c)Percentual de pessoas com salário menor que R$ 1000: {perc_salario}%")
