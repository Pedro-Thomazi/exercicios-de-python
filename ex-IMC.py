nome = str(input('Digite seu nome: '))
print('------------------------------')
altura = float(input('Digite sua altura em metros: '))
print('------------------------------')
peso = float(input('Digite o seu peso: '))
print('------------------------------')
imc = peso / altura ** 2

print(
    f'Com a altura de {altura:.2f}m e o peso de {peso}kg, o {nome} tem o IMC de {imc:.2f}')
