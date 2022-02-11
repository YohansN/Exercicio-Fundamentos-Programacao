'''Q005: Dado os índices de massa corporal e sua classificação, conforme tabela abaixo, crie uma função
em python para ler os valores (peso e altura) de uma pessoa e mostrar seu IMC, CLASSIFICAÇÃO e OBESIDADE.'''

def imc(peso, altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        print(f"IMC: {imc:.2f} - Classificação: Magreza - Obesidade(grau): 0")
    elif 18.5 <= imc <= 24.9:
        print(f"IMC: {imc:.2f} - Classificação: Normal - Obesidade(grau): 0")
    elif 25 <= imc <= 29.9:
        print(f"IMC: {imc:.2f} - Classificação: Sobrepeso - Obesidade(grau): I")
    elif 30 <= imc <= 39.9 :
        print(f"IMC: {imc:.2f} - Classificação: Obesidade - Obesidade(grau): II")
    elif 40 <= imc:
        print(f"IMC: {imc:.2f} - Classificação: Obesidade Grave - Obesidade(grau): III")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metro: "))
imc(peso, altura)