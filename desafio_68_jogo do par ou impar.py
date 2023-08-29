from random import randint

v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': 
        tipo = str(input('Par ou Impar?[P/I]: ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. total de {}'.format(jogador, computador,total))
    if tipo == 'P':
        if total % 2 == 0:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você VENCEU!')
            v += 1
        else:
            print('você PERDEU!')
            break
        print('vamos jogar novamente...')
    print('GAME OVER! você venceu {} vezes.'.format(v))
