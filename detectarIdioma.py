# Script que detecta o idioma de cada linha de texto do arquivo original
# e retorna um arquivo com o texto e a classificação ao lado de cada linha

import pycld2 as cld2

with open('textoInicial.txt','r') as arquivoInicial, open('textoFinal.txt','a+') as arquivoFinal:
    for a in arquivoInicial:
        text_content = (a)
        textoLimpo = text_content.strip('\n')
        _, _, _, detected_language = cld2.detect(textoLimpo, returnVectors=True)
        aLimpo = a.strip('\n')
        arquivoFinal.write(f'{aLimpo}\t{detected_language}\n')