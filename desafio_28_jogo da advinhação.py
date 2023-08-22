from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador sortear
print('-=-'*10)
print('Vou pensar em um número entre 0 e 5. tente advinhar...')
print('-=-'*10)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar
print('processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Ganhei!, Eu pensei no número {}, não no número {}'.format(computador, jogador))
