# Script que separa frases delimitadas por "|" em linhas distintas 

with open('comPipes.txt','r') as arquivoInicial, open('separado.txt','a+') as arquivoFinal:
    for linha in arquivoInicial:
        inicio = str(linha).split(' | ')
        b = str(inicio[0]) + ' | '
        print(b, len(b))
        for a in range(1, len(inicio)-1):
            if len(b) > 20:
                arquivoFinal.write(f'{b}\n')
                b = ''
            b+= str(inicio[a]) + ' | '