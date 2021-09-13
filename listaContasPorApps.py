# Script que abre as listas de apps por contas (appsContas.txt) e de apps (apps.txt)
# e cruza os dados para criar outra lista (contasApps.txt) com apps e respectivas contas
# que usam cada app

dicionario = {}

with open('appsContas.txt','r') as arquivoConApps, open('contasApps.txt','a+') as arquivoFinal:   
    for linha in arquivoConApps:
        linhaLimpa = linha.split()
        conta = linhaLimpa[0].strip('[],\'')
        for item in range(1, len(linhaLimpa)-1):
            if linhaLimpa[item] not in dicionario:
                dicionario[linhaLimpa[item]] = set()
            dicionario[linhaLimpa[item]].add(conta)
    for a, b in dicionario.items():
        aLimpo = str(a).strip('[],\'\{\}')
        bLimpo = str(b).strip('[],\'\{\}')
        arquivoFinal.write(f'{aLimpo}\t{bLimpo}\n')