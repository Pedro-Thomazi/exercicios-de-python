"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite apenas horas: ')
min = input('Digite apenas os minutos: ')

hora_int = int(hora)
min_int = int(min)

if hora_int <= 11:
    print(f'Bom dia. São {hora_int}:{min_int}')

elif hora_int <=17:
    print(f'Boa tarde. São {hora_int}:{min_int}')

elif hora_int <= 23:
    print(f'Boa noite. São {hora_int}:{min_int}')

else: 
    print(f'ERRO... Hora ou minuto não correspondem a realidade.')

