"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra = 'Arroz'.lower()
palavra_escondida = ''
letras_acertadas = ''
tentativas = 0
cont = 0



while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        letras_acertadas += letra
        tentativas += 1
    else:
        tentativas += 1

    palavra_formada = ''
    for l in palavra:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == palavra:
        os.system('cls')
        print('--------------------')
        print('VOCÊ GANHOU!!!!!!!!')
        print(f'A palavra era {palavra}')
        break

print(f'Total de tentativas: {tentativas}')