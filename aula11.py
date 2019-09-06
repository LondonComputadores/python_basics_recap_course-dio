
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[3]
    #x = a
    #print('fechando arquivo')
    #arquivo.close() #foi colocado aqui somente paar efeito de explcação 
    #mas não pode ser usado aqui e o correto é usar no finally abaixo
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0.')
except ArithmeticError:
    print('Houve um erro ao realizar a operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
