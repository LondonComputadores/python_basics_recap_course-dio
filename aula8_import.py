
from aula8 import Televisao
from aula8_contaletras_lambda import conta_letras, teste

#Sem o if abaixo e sem a identação em seguida funciona
#do mesmo jeito

if __name__ == "__main__":

    tela = Televisao()
    print(tela.ligada)
    tela.power()
    print(tela.ligada)

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = conta_letras(lista)
    print('Total de Letras por Palavra: {}'.format(total_letras))

    print(teste())



'''
    from aula8 import Televisao
    from aula7 import Calculadora

    tela = Televisao()
    print(tela.ligada)
    tela.power()
    print(tela.ligada)

    calc = Calculadora(5, 10)
    print(calc.soma())

    #OBS.: pra isso funcionar tem que adicionar
    #o 'if __name__ == "__main__":' assim
    #como na aula8.py!
'''