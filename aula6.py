# conjunto = {1,2,3,4,4,2}
# conjunto.add(5)
# print(conjunto)

# conjunto.discard(2)
# print(conjunto)

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_intersecao = conjunto.intersection(conjunto2)
print(conjunto_intersecao)
conjunto_diferença1 = conjunto.difference(conjunto2)
conjunto_diferença2 = conjunto.difference(conjunto)
print('Diferenca entre 1 e 2: {}'.format(conjunto_diferença1))
print('Diferenca entre 1 e 2: {}'.format(conjunto_diferença2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simetrica: {}'.format(conjunto_diff_simetrica))

#subset
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

#superset
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_b.issuperset(conjunto_a)
print(conjunto_subset)

#transformar lista em conjunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)