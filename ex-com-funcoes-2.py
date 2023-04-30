# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

num = float(input('Digite um número: '))
mult = float(input('Digite o multiplicador: '))

# def duplicar():
#     return f'O número: {num} x 2 = {num * 2}'
# def triplicar():
#     return f'O número: {num} x 3 = {num * 3}'
# def quaduplicar():
#     return f'O número: {num} x 4 = {num * 4}'

def fazer_conta():
    return f'{num} x {mult} = {num * mult}'

print(fazer_conta())
