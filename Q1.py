import os
import csv

#lembrar de trocar o diretorio para o da pasta onde se encontram os arquivos de compra
path = '/Users/renan/OneDrive/Documentos/IME/Engenharia Elétrica/1º SEM/PEE/VF/Q1/Compras'

files = os.listdir(path)

#abrindo 2 arquivos: um para auxiliar na formação do arquivo do relatorio e outro com o proprio resumo
y = open('Auxiliar.txt', 'w')
z = open('Resumo.txt', 'w')
for file in files:
    y.write(file + ':\t')
    z.write(file + ':\n')

    onlyfiles = next(os.walk(path))[2]
    indicador = 0
    #recorrencia para ler e passar para os txt todos os arquivos csv, independente da quantidade
    if indicador < len(onlyfiles):
        #Abrindo os arquivos csv
        with open(path + '/' + file) as csv_file:
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

#criando o arquivo do relatorio
x.write('Itens superfaturados:\n\n')
caderno = {}
for linha in y:
    item = linha.split('\t')
    caderno[item[0]] = item
    print(caderno[item[0]])

#Programa não terminado
