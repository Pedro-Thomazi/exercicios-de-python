nome = str(input('Digite seu nome: '))
idade = str(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Nada foi digitado')
    