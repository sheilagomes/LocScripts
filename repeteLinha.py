# Script para repetir o conteúdo de cada linha para que tenha no mínimo 40 caracteres

with open('VTEXi18.txt','r') as arquivoInicial, open('repetido.txt','a+') as arquivoFinal:
    b = ''
    for linha in arquivoInicial:
        linhaLimpa = linha.strip('\n')
        while len(b) < 40:
            b+= (f'{linhaLimpa} ')
        arquivoFinal.write(f'{b}\n')
        b = ''