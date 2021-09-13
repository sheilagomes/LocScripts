# Script que cria arquivos *.txt com categorias globais
# em formato par chave-valor, de acordo com os idiomas na
# lista idiomas.txt que correspondem a arquivos csv na pasta CSV

import csv

with open("idiomas.txt","r") as ref_arquivo:
    for linha in ref_arquivo:
        linhaLimpa = str(linha).strip()
        csvIdioma = (f'CSV/{linhaLimpa}')
        txtIdioma = (f'{linhaLimpa.split(".", 1)[0]}.txt')
        with open(txtIdioma, 'a') as language:
            with open(csvIdioma) as csvfile:
                csvLanguage = csv.reader(csvfile)
                for row in csvLanguage:
                    rowIndex = -1
                    while True:
                        if row[rowIndex] == '':
                            rowIndex-=1
                        else:
                            language.write(str(f'\"category-id-{row[0]}\": \"{row[rowIndex]}\",'))
                            break