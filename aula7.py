#Métodos, funções e classes

#Exemplo 1
def soma(a, b):
        return a + b

def subtracao(a, b):
        return a - b

def multiplicacao(a, b):
        return a * b

def divisao(a, b):
        return a / b

print(soma(1, 2))
print(soma(3, 4))
print(subtracao(10,2))
print(multiplicacao(10,2))
print(divisao(10,2))

print('##############################################################')

#Exemplo 2
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

#instanciação de classes
calc = Calculadora(10, 2)
print(calc.valor_a)
print(calc.soma())
print(calc.subtracao())
print(calc.multiplicacao())
print(calc.divisao())

print('##############################################################')

#Exemplo 3
class Calculadora:
    
    def soma(self, valor_a , valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a , valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a , valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a , valor_b):
        return valor_a / valor_b

#instanciação de classes
calc = Calculadora()
print(calc.soma(10, 2))
print(calc.subtracao(10, 2))
print(calc.multiplicacao(10, 2))
print(calc.divisao(10, 2))

print('##############################################################')

#Exemplo 4 - Televisão

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

tela = Televisao()
print('Televisao está ligada: {}'.format(tela.ligada))
tela.power()
print('Televisao está ligada: {}'.format(tela.ligada))
tela.power()
print('Televisao está ligada: {}'.format(tela.ligada))

tela.power()
print('Televisao está ligada: {}'.format(tela.ligada))
print('Canal: {}'.format(tela.canal))
tela.aumenta_canal()
tela.aumenta_canal()
print('Canal: {}'.format(tela.canal))
tela.diminui_canal()
print('Canal: {}'.format(tela.canal))