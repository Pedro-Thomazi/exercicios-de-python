
# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# -------------------------------------------MINHA RESOLUÇÂO-------------------------------------
while True:
    acertos = 0
    erros = 0
    for pergunta in perguntas:
        indice = 1
        print(' ')
        print('Pergunta: ', pergunta['Pergunta'])
        print(' ')
        print('Opções: ')
        for opcao in pergunta['Opções']:
            print(f'{indice}) {opcao}')
            indice += 1
        resp = input('Resposta: ')
        if resp == pergunta['Resposta']:
            print('Acertou')
            acertos += 1
        else:
            print('ERROUU')
            erros += 1
        print('-------------------')

    print(f'Você ACERTOU: {acertos} e ERROU: {erros}')
    
    recomecar = input('Você quer recomecar? [s]im: ').lower()
    if recomecar == 's':
        continue
    else:
        print('FIM')
        break

# -------------------------------------------OUTRA RESOLUÇÂO-------------------------------------
# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta: ', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i}) {opcao}')
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou')
#     else:
#         print('Errou')

    
#     print()

# print(f'Você acertou {qtd_acertos}')
# print(f'de {len(perguntas)} perguntas')