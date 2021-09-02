# Script que abre uma lista (GERAL.txt) e extrai palavra por palavra,
# colocando o resultado em outra lista (GERALexclusiva.txt), filtrando se já tem igual, 
# se não é só números e se tem "vtex" como parte do nome

import re 

arquivoLeitura = open("GERAL.txt","r")
arquivoEscrita = open("GERALexclusiva.txt","a+")

for linha in arquivoLeitura:
    linhaLimpa = str(linha).strip().split()
    for i in range(0, len(linhaLimpa)):
        if linhaLimpa[i] not in arquivoEscrita and re.search("[0-9]\.[0-9]", linhaLimpa[i]) == None and 'vtex' in linhaLimpa[i]:
            arquivoEscrita.write(f'{linhaLimpa[i]}\n')

arquivoLeitura.close()
arquivoEscrita.close()