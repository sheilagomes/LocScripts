# Entra nas contas da lista contas.txt (que tem um nome de conta por linha) e cria um arquivo com a lista de apps usados pela conta. Vai abrir a conta pelo navegador e é preciso validar manualmente a entrada em cada conta, para evitar problemas por excesso de login

import os

with open('contas.txt','r') as ref_arquivo:
    for linha in ref_arquivo:
        comando1 = (f'vtex switch {linha}')
        comando2 = (f'vtex ls >{linha}.txt')
        os.system(comando1)
        os.system(comando2)