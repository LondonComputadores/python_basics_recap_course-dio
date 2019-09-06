class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

#print(__name__)

if __name__ == "__main__":
    
    tela = Televisao()
    print('Televisao está ligada: {}'.format(tela.ligada))
    tela.power()
    print('Televisao está ligada: {}'.format(tela.ligada))
    tela.power()
    print('Televisao está ligada: {}'.format(tela.ligada))

    tela.power()
    print('Televisao está ligada: {}'.format(tela.ligada))
    print('Canal: {}'.format(tela.canal))
    tela.aumenta_canal()
    tela.aumenta_canal()
    print('Canal: {}'.format(tela.canal))
    tela.diminui_canal()
    print('Canal: {}'.format(tela.canal))