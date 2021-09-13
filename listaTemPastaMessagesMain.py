# Script temporário que extrai informações de contas dentro
# do arquivo GERALexclusiva.txt e cria um novo arquivo
# listaMessages.txt com as informações separadas por tabulações
# Temporário porque não é o ideal, já que toma conta do computador
# e outras atividades não podem ser feitas durante a execução.

import pyautogui, time, re, clipboard

listaResultado = []
listaApps = open("GERALexclusiva.txt","r")
listaMessages = open("listaMessages.txt","a+")

def copiaPagina():
    pyautogui.click(1347, 126)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

for linha in listaApps:
    linhaLimpa = str(linha).strip().split('.')
    nomeApp = linha.strip()
    urlParcial = (f'{linhaLimpa[0]}/{linhaLimpa[1]}/')
    urlGithub = (f'https://github.com/{urlParcial}tree/main/messages')
    clipboard.copy(urlGithub)
    copiaPagina()
    conteudoPagina = clipboard.paste()
    listaConteudo = conteudoPagina.split()
    for n in listaConteudo:
        if 'json' in n and n != 'context.json' and n not in listaResultado:
            n = n.replace('.json', '')
            listaResultado.append(n)
    if listaResultado:
        listaMessages.write(f'{nomeApp}\t{urlGithub}\t{listaResultado}\n')
        listaResultado = []
    else:
        listaMessages.write(f'{nomeApp}\t\t\n')
pyautogui.hotkey('alt', 'tab')
listaApps.close()
listaMessages.close()