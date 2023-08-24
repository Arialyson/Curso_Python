n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('-='*10)
if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n1 < n2:
    print('O SEGUNDO valor é maior!')
elif n1 == n2:
    print('Os valores são IGUAIS')
