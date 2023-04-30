
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# Ex.:  195.868.480-51 (195868480)
#    10  9  8  7  6  5  4  3  2
# *  1   9  5  8  6  8  4  8  0
#    10  81 40 56 36 40 16 24 0


# Ex.:  195.868.480-51 (195868480)
#    11  10  9  8  7  6  5  4  3  2
# *  1   9   5  8  6  8  4  8  0  5
#    11  90  45 64 42 48 20 32 0  10

#  -------------------------------------------------------------------------------------
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
import re
import sys

soma_dos_numeros = 0

# cpf_enviado_usuario = '19586848051'

# cpf_enviado_usuario = '195.868.480-51' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '') 
entrada = input('CPF [195.868.480-51]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]', # tudo que não for número
    '', # substitui para...
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contado_regressivo = 10

for digito in nove_digitos:
    soma_dos_numeros += int(digito) * contado_regressivo
    contado_regressivo -= 1
mult_da_soma = soma_dos_numeros * 10
resto_da_div = mult_da_soma % 11

ultimo_digito = resto_da_div 
peultimo_digito = ultimo_digito if ultimo_digito <= resto_da_div else 0

# -----------------------------------------------------------------------------------------------

dez_digitos = cpf_enviado_usuario[:10]
contado_regressivo = 11
soma_dos_numeros = 0

for digito in dez_digitos:
    soma_dos_numeros += int(digito) * contado_regressivo
    contado_regressivo -= 1
mult_da_soma_por_dez = soma_dos_numeros * 10
resto_da_div = mult_da_soma_por_dez % 11
ultimo_digito = resto_da_div
ultimo_digito + ultimo_digito if ultimo_digito <= resto_da_div else 0

cpf_gerado = f'{nove_digitos}{peultimo_digito}{ultimo_digito}'

print('---------------------------------------------------------------------------------')
if cpf_enviado_usuario == cpf_gerado:
    print(f'{nove_digitos}{peultimo_digito}{ultimo_digito} é valido')
else:
    print('CPF invalido')

print('---------------------------------------------------------------------------------')