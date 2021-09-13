# Script que abre as listas de contas (contas.txt) e de apps (GERALexclusiva.txt)
# e cruza os dados para criar outra lista (appsContas.txt) com as contas que usam
# cada app

import re 

with open("contas.txt","r") as arquivoContas, open("apps.txt","r") as arquivoApps,  open("appsContas.txt","a+") as arquivoFinal:
    appsContas = []
    for linha in arquivoContas:
        linhaLimpa = str(linha).strip()
        appsContas.append(linhaLimpa)
        caminhoConta = (f'AppsContas/{linhaLimpa}')
        with open(caminhoConta, "r") as contaTemp:
            for item in contaTemp:
                itemLimpo = str(item).strip().split()
                for linhaItem in range(0, len(itemLimpo)-1):
                    if not re.compile("[0-9]\.[0-9]").match(itemLimpo[linhaItem]) and "vtex" in itemLimpo[linhaItem]:
                        appsContas.append(itemLimpo[linhaItem])
        arquivoFinal.write(f'{appsContas}\n')
        appsContas = []