'''Q004: O sistema do governo quer verificar um grupo de empregados apto para a aposentadoria ou não.
Para estar em condições, os seguintes requisitos devem ser satisfeitos: - Ter no mínimo 65 anos de
idade e ter trabalhado no mínimo 35 anos – homens; ter 60 anos de idade e ter trabalhado 30 anos -
mulheres. Com base nessas informações, faça um algoritmo que leia (para 6 empregados): o nome,
sexo, ano de nascimento e os anos de contribuições. O programa deverá escrever: nome, idade, sexo e
o tempo de trabalho de cada empregado com a mensagem 'Apto para aposentadoria' ou 'Não apto
para aposentadoria'.'''

ano_atual = 2021
for i in range(1, 7):
    nome = str(input("Qual seu nome? "))
    sexo = str(input("Qual seu sexo biológico? [ M / F ] ").upper())
    ano_nascimento = int(input("Em que ano você nasceu? "))
    idade = ano_atual - ano_nascimento
    tempo_trabalhado = int(input("Quantos anos de contribuição? "))
    
    print("-------------------------------------")
    print(f"Ficha do empregado:\nNome: {nome}.\nIdade: {idade} anos.\nSexo biológico: {sexo}.\nTempo de trabalho: {tempo_trabalhado} Anos.")
    if(sexo == "M"):
        if(idade >= 65 and tempo_trabalhado >= 35):
            print("Apto para aposentadoria")
        else:
            print("Não apto para aposentadoria")
    elif(sexo == "F"):
        if(idade >= 60 and tempo_trabalhado >= 30):
            print("Apto para aposentadoria")
        else:
            print("Não apto para aposentadoria")
    else:
        print("Erro: Sexo invalido. Tente novamente")
    print("-------------------------------------")
