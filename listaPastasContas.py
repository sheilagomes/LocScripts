import pyautogui, time, clipboard
from bs4 import BeautifulSoup

def copiaPagina():
    pyautogui.click(1297, 126)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'u')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.5)

with open('repos.txt','r') as arquivoInicial, open('temSRC.txt','a+') as arquivoFinal:
    for linha in arquivoInicial:
        linhaLimpa = str(linha).strip().split('.')
        urlParcial = (f'{linhaLimpa[0]}/{linhaLimpa[1]}/')
        urlGithub = (f'https://github.com/{urlParcial}')
        clipboard.copy(urlGithub)
        copiaPagina()
        conteudoPagina = clipboard.paste()
        arquivoFinal.write(f'{urlGithub}\n')
        bsObj = BeautifulSoup(conteudoPagina, "html.parser")
        lista = bsObj.find_all('a', {'class':"js-navigation-open Link--primary"})
        for text in lista:
            conteudoClasse = text.get_text()
            arquivoFinal.write(f'{conteudoClasse}\n')
        if not lista:
            arquivoFinal.write(' - Esta página não existe ou o repositório não tem arquivos')
        arquivoFinal.write(f'\n========================\n')

pyautogui.hotkey('alt', 'tab')