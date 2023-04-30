nome = str(input('Digite seu nome: '))
len_nome = len(nome)

contador = 0
novo_nome = ''

while contador < len_nome:
    novo_nome += f'*{nome[contador]}'
    contador += 1
print(novo_nome)