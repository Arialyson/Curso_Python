from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qualé a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:#computador jogou pedra
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('jogada INVÁLIDA!')
elif computador == 1: #computador jogou papel
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCE')
    else:
        print('jogada INVÁLIDA!')
elif computador == 2: #computador jogou tesoura
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('jogada INVÁLIDA!')