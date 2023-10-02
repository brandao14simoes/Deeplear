from time import sleep
from threading import Lock, Thread

import os 

os.system('cls')


# 324. (Parte 2) Threads - Executando processamentos em paralelo
'''
class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1', 3)
t1.start()

t2 = MeuThread('Thread 2', 6)
t2.start()

t3 = MeuThread('Thread 3', 9)
t3.start()


for MeuThread in range(10):
    print(MeuThread)
    sleep(1)
'''
# ------------------TESTE -------------------
# print('Hello')

# for Hello in range(10):
#     print("Hello")
#     sleep(5)

# print('World')

# 325. (Parte 2) Threads - Executando processamentos em paralelo
'''
def vaidemorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vaidemorar, args=('Vai', 3))
t1.start()

t2 = Thread(target=vaidemorar, args=('Demorar', 6))
t2.start()

t3 = Thread(target=vaidemorar, args=('um Pouco!', 9))
t3.start()

for Thread in range(20):
    print(Thread)
    sleep(.5)
'''
'''
def vaidemorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vaidemorar, args=('You Win!', 10))
t1.start()
#t1.join() Bloqueio de Thread

# while t1.is_alive():
#     print('Loanding...')
#     sleep(2)

print('Thread Acabou')
'''

#326. (Parte 3) Threads - Executando processamentos em paralelo

class Ingressos:
    """
    Classe que vende Ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :parar estoque: quantidade de ingressos em estoque.
        """
        self.estoque = estoque
        # Nossa cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Comprar determinado quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o Método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            #libera o Método
            self.lock.release()
            return
        sleep(2)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'\nAgora restam apenas {self.estoque}. ')
        #libera o metodo
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)

    for Ingressos in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(Ingressos,))
        t.start()
    print(ingressos.estoque)