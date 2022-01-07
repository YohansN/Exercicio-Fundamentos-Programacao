'''Q003: Faça um algoritmo para ler o saldo de 5 clientes. Depois, deverá realizar operações de débito e
crédito: lê um crédito aleatório para cada cliente; realizar saque (débito qualquer) da conta de cada
cliente; (saldo_atual = crédito - débito). Também testar se saldo atual é suficiente para realizar o saque,
confirmando a operação, caso positivo, e negando a operação, caso negativo, mostrando a mensagem
'Saldo insuficiente'. No final, deverá exibir o saldo atualizado de cada cliente.'''

saldo = 0
for i in range(1, 6):
  print(f"{i}° Cliente: ")
  credito = int(input("Digite o valor do crédito: R$ "))
  saldo = saldo + credito
  print(f"Saldo: R${saldo}")
  saque = int(input("Digite o valor do saque: "))
  if(saque > saldo):
    print("Saldo insuficiente")
  else:
    saldo = saldo - saque
  print(f"Saldo atual: R$ {saldo}")
  print("------------------------------")
  saldo = 0
