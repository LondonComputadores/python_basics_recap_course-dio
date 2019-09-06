a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
resto_a = a % 2
resto_b = a % 2
#if resto == 0:
if resto_a == 0 or not resto_b > 0:
    print('numero é par!')
else:
    print('número é ímpar!')