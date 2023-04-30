""" Calculador com While """

while True:
    num1 = (input('Digite um número: '))
    operador = (input('Digite um operador(+ - / *): '))
    num2 = (input('Digite outo número: '))

    nums_validos = None
    num_1_float = 0
    num_2_float = 0

    try: 
        num_1_float = float(num1) 
        num_2_float = float(num2)
        nums_validos = True
    except:
        nums_validos = None

    if nums_validos is None:
        print('Um ou ambos os números são invalidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ##########
    print('Realizando a conta...')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    else:
        print('ERRO..... Não deveria ter chegado aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break