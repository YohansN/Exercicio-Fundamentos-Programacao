'''Q001: Deseja-se atualizar as contas correntes dos clientes de uma agência bancária.
É dado o cadastro de 5 clientes contendo para cada um as seguintes informações: o número da conta, nome, saldo e OP (pode ser C ou D).
Implemente uma matriz 5 x 5 que mostre o movimento bancário de cada um desses clientes.'''

banco = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #Matriz 5x5
saldo_final = []

for i in range(0, 5):
    print(f"{i + 1}° Cliente: ")
    for j in range(0, 5):
        if j == 0:
            banco[i][j] = int(input("Número da conta: "))
        elif j == 1:
            banco[i][j] = str(input("Nome:").upper())
        elif j == 2:
            banco[i][j] = float(input("Saldo: "))
            saldo = banco[i][j]
        elif j == 3:
            banco[i][j] = float(input("Credito: "))
            saldo = saldo + banco[i][j]
        elif j == 4:
            banco[i][j] = float(input("Débito: "))
            saldo = saldo - banco[i][j]
            saldo_final.append(saldo)
    print("--" * 20)

print("|N° conta| |Nome| |Saldo Inicial| |Saldo final|")
for i in range(0, 5):
    for j in range(0, 3):
        print(f"| {banco[i][j]} |", end=' ')
    print(f"| {saldo_final[i]} |", end=' ')
    print("\n")
