lista = [1, 2, 4, 5]
lista_animals = ['dog', 'cat', 'bird']
print(lista)
print(lista_animals[2])

print(sum(lista))
print(max(lista))
print(min(lista_animals))
print(max(lista_animals))

if 'eagle' in lista_animals:
    print('Oh yeah!')
else:
    print('No way!')
    lista_animals.append('eagle')
    print(lista_animals)

lista_animals.pop()
print(lista_animals)

lista.sort()
lista_animals.sort()
print(lista, lista_animals)

lista.reverse()
lista_animals.reverse()
print(lista, lista_animals)

lista_animals[0] = 'monkey'
print(lista_animals)

tupla = (1, 2, 3, 4)
print(tupla[2])
print(len(tupla))

tupla_animals = tuple(lista_animals)
print(type(tupla_animals))
print(tupla_animals)
#tupla_animals[0] = 'fish' #erro pq tupla é imutavel

tupla_numerica = list(tupla)
print(type(tupla_numerica))
tupla_numerica[0] = 100
print(tupla_numerica)


