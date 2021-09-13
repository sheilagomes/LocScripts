# Script que valida o texto dentro de cada arquivo em uma pasta
#  para ver se o conteúdo corresponde ao nome do arquivo

conferidoOk, naoConsta = [], []

with open("contas.txt","r") as ref_arquivo:
    for linha in ref_arquivo:
        linhaLimpa = str(linha).strip()
        valida = open(linhaLimpa,"r")
        if linhaLimpa in valida.readline():
            conferidoOk.append(linhaLimpa)
        else:
            naoConsta.append(linhaLimpa)
        valida.close()