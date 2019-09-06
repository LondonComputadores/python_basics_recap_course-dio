a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Segundo valor: '))

if a > b:
    print('O maior número é {}' .format(a))
elif b > a and b > c:
    print('O maior número é {}' .format(b))
else:
    print('O maior número é {}' .format(c))
print('final do programa')