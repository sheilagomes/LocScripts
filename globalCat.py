# Script que cria arquivos *.txt com categorias globais
# em formato par chave-valor, de acordo com os idiomas na
# lista idiomas.txt que corrspondem a arquivos csv na pasta CSV


import csv

ref_arquivo = open("idiomas.txt","r")

for linha in ref_arquivo:
    linhaLimpa = str(linha).strip()
    csvIdioma = (f'CSV/{linhaLimpa}')
    txtIdioma = (f'{linhaLimpa.split(".", 1)[0]}.txt')
    language = open(txtIdioma, 'a')
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
    language.close()
ref_arquivo.close()