'''Q003: Faça um algoritmo para ler o preço unitário e a quantidade de um produto e imprimir o valor total desse
produto.'''

unidade = float(input("Preço da unidade:"))
quantidade = int(input("Quantidade do produto: "))
preço = (unidade * quantidade)
print(f"O valor total é: R${preço:.2f}")
