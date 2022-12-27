# Extrai informações das pastas messages dos apps no arquivo GERALexclusiva.txt e cria um novo arquivo listaMessages.txt com as informações separadas por tabulações.

import pyautogui, time, re, clipboard

listaResultado = []

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

with open('GERALexclusiva.txt','r') as listaApps, open('listaMessages.txt','a+') as listaMessages:
    for linha in listaApps:
        linhaLimpa = str(linha).strip().split('.')
        nomeApp = linha.strip()
        urlParcial = (f'{linhaLimpa[0]}/{linhaLimpa[1]}/')
        urlGithub = (f'https://github.com/{urlParcial}tree/master/messages')
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