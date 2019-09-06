def conta_letras(word_list):
    contador = []
    for x in word_list:
        qtde = len(x)
        contador.append(qtde)
    return contador

def teste():
    return 'teste'

if __name__ == "__main__":
    lista = ['cachorro', 'gato']
    print(conta_letras(lista))

print('#######################################################')

#O método acima conta_letras pode ser feito utilizando o Lambda
# e reduzindo-o a uma única linha ao invés de 6 linhas.

conta_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print('Total de Letras por Animal é: {}'.format(conta_letras(lista_animais)))
print(conta_letras(lista_animais))

print('#######################################################')

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b 
print(soma(5, 10))
print(subtracao(10, 5)) 

print('#######################################################')

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b, 
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a,b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
print('A soma é: {}'.format(soma(10, 5)))
print('A subtracao é: {}'.format(subtracao(10, 5)))



