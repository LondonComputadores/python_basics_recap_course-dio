import shutil

def escrever_arquivo(texto):
    #diretorio = '/c/Users/londo/Documents/digital_innov_projects/notas.txt'
    #arquivo = open(diretorio, 'w')
    arquivo = open(notas.txt, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
    return lista_media

#Aqui estou apenas movendo o arquivo de um diretorio a outro (def copia e move e + mais abaixo move_arquivo('notas.txt'))
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/c/Users/londo/Documents/digital_innov_projects/fundamentos_python')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/c/Users/londo/Documents/digital_innov_projects/')

if __name__ == '__main__':
    #media_notas('notas.txt')
    move_arquivo('notas.txt')
    #escrever_arquivo('Mais uma linha\n')
    #aluno = 'Alex,10,9,8,7'
    #aluno = '\nMaria,9,8,7,9'
    #aluno = '\nJamie,9,8,7,6'
    #aluno = '\nMaya,8,7,6,5'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('notas.txt')