# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_v8 = Motor('v8')
fusca.fabricante = volkswagen
fusca.motor = motor_v8
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)

print()

fiat_uno = Carro('Fiat Uno')
fiat = Fabricante('Fiat')
motor_v8 = Motor('v8')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_v8
print(fiat_uno.nome, fiat_uno.motor.nome, fiat_uno.fabricante.nome)

print()

focus = Carro('Focus')
ford = Fabricante('Ford')
motor_v8 = Motor('v6')
focus.fabricante = ford
focus.motor = motor_v8
print(focus.nome, focus.motor.nome, focus.fabricante.nome)

print()
