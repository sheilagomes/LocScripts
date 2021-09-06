# Este programa extrai o texto de todos os arquivos em uma pasta, conforme os parâmetros após as linhas
# "for f in filenames:" e "for line in txtfile:" e coloca tudo em um arquivo output.txt na mesma pasta.
# Alterar o caminho para a pasta na variável ab, se for necessário.

import os

ab = 'c:/users/sheila/desktop/testepy'
with open('c:/users/sheila/desktop/testepy/output.txt', 'w') as output_file :
    output = {}
    file_list = []
    for (dirpath, dirname, filenames) in os.walk(ab):
        for f in filenames:
            if 'por-BR' in str(f):
                e = os.path.join(str(dirpath), str(f))
                file_list.append(e)
                
    for f in file_list:
        print(f)
        txtfile = open(f, 'r', encoding="utf8")
        output[f] = []
        for line in txtfile:
            if 'title' in line:
                output[f].append(line)
            if 'description' in line:
                output[f].append(line)
            if 'tags' in line:
                output[f].append(line)
    tabs = []
    for tab in output:
        tabs.append(tab)

    #tabs.sort()
    for tab in tabs:
        for row in output[tab]:
            output_file.write(row + '')
