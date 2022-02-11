'''Q004: Ler um formato de número inteiro e verificar se o número corresponde a uma data válida no
calendário. Em seguida, escrever “Data Válida, 10 de julho de 2020, p.ex”; senão escrever uma
mensagem “Data Inválida”.'''

def mes_nome(mes): #Função que transforma o número do mês no nome do mês
    global nmes #definindo nmes como global para que ela possa existir como uma variável fora dessa função.
    if mes == '01':
        nmes = 'Janeiro'
    elif mes == '02':
        nmes = 'Fevereiro'
    elif mes == '03':
        nmes = 'Março'
    elif mes == '04':
        nmes = 'Abril'
    elif mes == '05':
        nmes = 'Maio'
    elif mes == '06':
        nmes = 'Junho'
    elif mes == '07':
        nmes = 'Julho'
    elif mes == '08':
        nmes = 'Agosto'
    elif mes == '09':
        nmes = 'Setembro'
    elif mes == '10':
        nmes = 'Outubro'
    elif mes == '11':
        nmes = 'Novembro'
    elif mes == '12':
        nmes = 'Dezembro'
    else:
        print("Mês invalido")

def calendario(data_cortada):   #Função que manipula o input do usuário mexendo na string para separar dia, mês e ano.
    separador = ''
    dia = []
    mes = []
    ano = []
    if len(data_cortada) == 7: #datas em que o primeiro digito é zero(0)
        #DIA
        dia = data_cortada[0]
        #MÊS
        for i in range(1, 3):
            mes.append(data_cortada[i])
        mes = separador.join(mes)
        mes_nome(mes)
        #ANO
        for i in range(3, 7):
            ano.append(data_cortada[i])
        ano = separador.join(ano)
        print(f"Data válida, 0{dia} de {nmes} de {ano}.")
    
    elif len(data_cortada) == 8:
        #DIA
        for i in range(0,2):
            dia.append(data_cortada[i])
        dia = separador.join(dia) #Junta os números correspondentes ao dia.
        #MÊS
        for i in range(2,4):
            mes.append(data_cortada[i])
        mes = separador.join(mes)
        mes_nome(mes)
        #ANO
        for i in range(4, 8):
            ano.append(data_cortada[i])
        ano = separador.join(ano)
        print(f"Data válida, {dia} de {nmes} de {ano}.")

num = int(input("Digite uma data, apenas números, 8 digitos no padrão DD-MM-AAAA: "))
if type(num) == int and len(str(num)) == 7 or len(str(num)) == 8 :    #Checa se a data é valida, sendo um número inteiro e de tamanho 5 ou 6 digitos
    data = str(num)
    data_cortada = list(data)   #separa a str da data em caracteres
    #print(data_cortada)
    calendario(data_cortada)
else:
    print("Data invalida.")