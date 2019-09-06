#a = 10
#b = 5

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('Soma: {}. \nSubtracao: {}'.format(soma, subtracao))
print('Soma: {soma}. \nSubtracao: {subtracao}'.format(soma=soma, subtracao=subtracao))