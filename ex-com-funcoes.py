# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    total = args[0]
    for num in args:
        total *= num
    print(total)


multiplicador(1, 2, 3, 4, 5)
print("----------------------")


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(*args):
    for num in args:
        if num % 2 == 0:
            print(f'{num} é par')
        else:
            print(f'{num} é ímpar')

par_ou_impar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    