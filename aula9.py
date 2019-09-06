# arquivo = open('aula9_teste.txt', 'w')
# arquivo.write('Minha primeira escrita\n')
# arquivo.close()

# arquivo = open('aula9_teste.txt', 'a')
# arquivo.write('\nMinha segunda escrita\n')
# arquivo.close()

#print('##############################################')

# def escrever_arquivo(texto):
#     arquivo = open('aula9_teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()

def escrever_arquivo(texto):
    diretorio = '/c/Users/londo/Documents/digital_innov_projects/teste2.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('/c/Users/londo/Documents/digital_innov_projects/teste2.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrever_arquivo('Mais uma linha\n')
    atualizar_arquivo('Mais outra linha\n')
    ler_arquivo('/c/Users/londo/Documents/digital_innov_projects/teste2.txt')
    #ler_arquivo('aula9_teste.txt')