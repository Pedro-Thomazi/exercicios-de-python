# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'


print('\033[30;42m-------------------Lista de tarefas-------------------\033[m')


lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
lista_de_deletados = []

while True:

    print()
    print('Comandos: listar - desfazer - refazer - sair')
    comando = input('Digite uma tarefa ou um comando: ').lower()
    print()
    if comando == 'listar':
        if len(lista_de_tarefas) == 0:
            print('Não tem terafas no momento.')
        else:
            for tarefa in lista_de_tarefas:
                print(f'- {tarefa}')
        continue

    elif comando == 'desfazer':
        if len(lista_de_tarefas) == 0:
            print('Não tem terafas no momento.')
        else:
            lista_de_deletados.append(lista_de_tarefas[-1])
            lista_de_tarefas.pop()
            for tarefa in lista_de_tarefas:
                print(f'- {tarefa}')
        continue

    elif comando == 'refazer':
        if len(lista_de_tarefas) == 0:
            print('Não tem terafas no momento.')
        else:
            if len(lista_de_deletados) == 0:
                for tarefa in lista_de_tarefas:
                    print(f'- {tarefa}')
                continue
            else:
                lista_de_tarefas.append(lista_de_deletados[-1])
                lista_de_deletados.pop()
                for tarefa in lista_de_tarefas:
                    print(f'- {tarefa}')
        continue

    elif comando == 'sair':
        print('Fim')
        break

    else:
        lista_de_tarefas.append(comando) 
        for tarefa in lista_de_tarefas:
            print(f'- {tarefa}')
            salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
        continue
    


    


# --------------------------------OU------------------------------------------------

# import json
# import os 


# def ler(tarefas, caminho_arquivo):
#     dados = []
#     try:
#         with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#             dados = json.load(arquivo)
#     except FileNotFoundError:
#         print('Arquivo não existe')
#         salvar(tarefas, caminho_arquivo)
#     return dados

# def salvar(tarefas, caminho_arquivo):
#     dados = tarefas
#     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#         dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
#     return dados


# CAMINHO_ARQUIVO = 'aula119.json'
# tarefas = ler([], CAMINHO_ARQUIVO)
# tarefas_refazer = []

# def desfazer(tarefas, tarefas_refazer):
#     if not tarefas:
#         print()
#         print('Nada a desfazer')
#         return
    
#     tarefa = tarefas.pop()
#     tarefas_refazer.append(tarefa)

# def refazer(tarefas, tarefas_refazer):
#     if not tarefas_refazer:
#         print()
#         print('Nada a refazer')
#         return
    
#     tarefa = tarefas_refazer.pop()
#     tarefas.append(tarefa)

# def adicionar(tarefa, tarefas):
#     tarefas.append(tarefa)

# def listar(tarefas):
#     print()
#     print('TAREFAS: ')
#     print(*tarefas, sep='\n')
#     print()

# while True:
#     print('Comandos: listar, desfazer, refazer')
#     tarefa = input('Digite uma tarefa ou um comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('cls'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }

#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()

#     salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue

    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue

    # elif tarefa == 'listar':
    #     listar(tarefas)
        
    # elif tarefa == 'clear':
    #     os.system('cls')
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue