'''Q002: A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais
de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%.
Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva
o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas,
em um total de 10 funcionários e depois mostre também qual destes obteve maior número de horas
trabalhadas. (considere um mês com 4 semanas exatas).'''

bonus = 0
hora_extra = 0
maior_horario = 0
salario_total = 0
salario_padrao = 0
trabalhador_num = 0
for i in range(1, 11):
    print(f"{i}º Trabalhador:")
    horas_mensais = int(input("Total de horas trabalhadas no mês: "))
    salario_hora = float(input("Valor salário hora: "))
    bonus = salario_hora * 150/100 #50% maior para cada hora extra trabalhada.
    if horas_mensais > 160:
        hora_extra = horas_mensais - 160
        salario_padrao = 160 * salario_hora
        salario_total = (160 * salario_hora) + (hora_extra * bonus)
        print(f"Salario: R$ {salario_padrao}. Acrescido de bonus: R$ {salario_total}")
        if maior_horario < horas_mensais:
            maior_horario = horas_mensais
            trabalhador_num = i #numero do trabalhador com mais horas.
    else:
        salario_padrao = 160 * salario_hora
        print(f"Salario: R$ {salario_padrao}.")
    print("-------------------------------")
print(f"O maior número de horas trabalhadas no mês foi de {maior_horario} horas, do {trabalhador_num}º trabalhador")
