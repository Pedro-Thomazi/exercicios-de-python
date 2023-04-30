import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    soma_dos_numeros = 0
    contado_regressivo = 10

    for digito in nove_digitos:
        soma_dos_numeros += int(digito) * contado_regressivo
        contado_regressivo -= 1
    mult_da_soma = soma_dos_numeros * 10
    resto_da_div = mult_da_soma % 11

    ultimo_digito = resto_da_div 
    penultimo_digito = ultimo_digito if ultimo_digito <= resto_da_div else 0

    # -----------------------------------------------------------------------------------------------

    dez_digitos = nove_digitos + str(penultimo_digito)
    contado_regressivo = 11
    soma_dos_numeros = 0

    for digito in dez_digitos:
        soma_dos_numeros += int(digito) * contado_regressivo
        contado_regressivo -= 1
    mult_da_soma_por_dez = soma_dos_numeros * 10
    resto_da_div = mult_da_soma_por_dez % 11
    ultimo_digito = resto_da_div
    ultimo_digito + ultimo_digito if ultimo_digito <= resto_da_div else 0

    cpf_gerado = f'{nove_digitos}{penultimo_digito}{ultimo_digito}'

    print('---------------------------------------------------------------------------------')
    print(cpf_gerado)
    print('---------------------------------------------------------------------------------')