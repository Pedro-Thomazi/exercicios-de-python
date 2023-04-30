"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = str(input('Digite seu primeiro nome: '))

nome_len = len(nome)

if nome_len <= 4:
    print('Seu nome é pequeno.')
elif nome_len <= 6:
    print('Seu nome é médio.')
else:
    print('Seu nome é grande.')
