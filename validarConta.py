conferidoOk, naoConsta = [], []
ref_arquivo = open("contas.txt","r")

for linha in ref_arquivo:
    linhaLimpa = str(linha).strip()
    valida = open(linhaLimpa,"r")
    if linhaLimpa in valida.readline():
        conferidoOk.append(linhaLimpa)
    else:
        naoConsta.append(linhaLimpa)
    valida.close()

ref_arquivo.close()
print("Não consta: ",naoConsta)
print("Confere: ",conferidoOk)