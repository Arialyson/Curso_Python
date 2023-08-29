n = 0
while True:
    n = int(input('quer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
    print('-'*30)
print('Tabuada encerrada, até a proxima!')
