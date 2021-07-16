import os
import csv

path = '/Users/renan/OneDrive/Documentos/IME/Engenharia Elétrica/1º SEM/PEE/VF/Q1/Compras'

files = os.listdir(path)

y = open('Auxiliar.txt', 'w')
z = open('Resumo.txt', 'w')
for file in files:
    y.write(file + ':\t')
    z.write(file + ':\n')

    #lembrar de trocar o diretorio para o da pasta onde se encontram os arquivos de compra
    onlyfiles = next(os.walk('/Users/renan/OneDrive/Documentos/IME/Engenharia Elétrica/1º SEM/PEE/VF/Q1/Compras'))[2]
    indicador = 0
    if indicador < len(onlyfiles):
        with open('/Users/renan/OneDrive/Documentos/IME/Engenharia Elétrica/1º SEM/PEE/VF/Q1/Compras/' + file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                y.write(row[0] + ', ' + row[1] + ', ' + row[2] + '\t')
                z.write(row[0] + ', ' + row[1] + ', ' + row[2] + '\n')
            y.write('\n')
            z.write('\n') 
        indicador = indicador + 1

z.write('\n')

y.close()
z.close()

y = open('Auxiliar.txt', 'r')
x = open('Relatorio.txt', 'w')

x.write('Itens superfaturados:\n\n')
caderno = {}
for linha in y:
    item = linha.split('\t')
    caderno[item[0]] = item
    print(caderno[item[0]])
