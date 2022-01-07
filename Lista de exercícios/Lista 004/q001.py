'''Q001: As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
escreva o custo total da compra. OBS: experimentar com menos de 12 e com mais de 12 quantidades.'''

macas = int(input("Número de maças compradas: "))
if macas < 12:
    preco = 1.3 * macas
    print("Preço unitário: R$ 1,30")
    print(f"Preço total: R$ {preco:.2f}")
elif macas >= 12:
    preco = 1 * macas
    print("Preço unitário: R$ 1,00")
    print(f"Preço total: R$ {preco:.2f}")
