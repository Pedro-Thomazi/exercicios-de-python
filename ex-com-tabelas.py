# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

print()
print('-------------------------------------Tabela original-------------------------------------')
print()
for produto in produtos:
    nome = produto['nome']
    preco = produto['preco']
    print(f'O produto "{nome}" R${preco:.2f}')


copia_dos_produtos = copy.deepcopy(produtos)
print()
print('-------------------------------------Tabela copiada-------------------------------------')
print()
for produto in copia_dos_produtos:
    preco_inicial = produto['preco']
    produto['preco'] *= 1.1
    nome = produto['nome']
    preco = produto['preco']
    print(f'O produto "{nome}" recebeu um aumento de 10%, e ficou R${preco:.2f}')



print()
print('-------------------------------------Tabela ordernada por preço-------------------------------------')
print()

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(copia_dos_produtos),
    key=lambda p: p['preco']
)

for produto in produtos_ordenados_por_preco:
    nome = produto['nome']
    preco = produto['preco']
    print(f'O produto "{nome}" R${preco:.2f}')





print()
print('-------------------------------------Tabela ordernada por nome-------------------------------------')
print()

produtos_ordenados_por_nome= sorted(
    copy.deepcopy(copia_dos_produtos),
    key=lambda p: p['nome']
)

for produto in produtos_ordenados_por_nome:
    nome = produto['nome']
    preco = produto['preco']
    print(f'O produto "{nome}" R${preco:.2f}')