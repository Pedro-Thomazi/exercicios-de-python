# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']



# def zipper(lista1, lista2):
#     intervalo_max = min(len(lista1), len(lista2))
#     return print([
#         {f'Cidade: {lista1[i]} - Estado: {lista2[i]}'} for i in range(intervalo_max)
#     ])

# zipper(cidades, estados)

#  ----------------------------------- ou --------------------------

# print(list(zip(cidades, estados))) # Pelo menor indice

# from itertools import zip_longest
# print(list(zip_longest(cidades, estados))) # Pelo maior indice


# ------------------------------------------------------------------------------------------------------------

"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7, 2, 7, 3, 1, 6, 7]
lista_b = [1, 2, 3, 4, 4, 7, 7, 12, 85, 2, 78, 2]

# def somar_nums(lista1, lista2):
#     intervalo_max = min(len(lista1), len(lista2))
#     return print([
#         {f'{lista1[i]} + {lista2[i]} = {lista1[i] + lista2[i]}'} for i in range(intervalo_max)
#     ])

# somar_nums(lista_a, lista_b)


#  ----------------------------------- ou --------------------------

lista_soma = []

# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# ------------------------------------------------------------

# for i, _ in enumerate(lista_b):  # retorna uma tupla
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# ------------------------------------------------------------

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)