tot18 = totH = totM20 = 0
while True:
    print('-='*15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    print('-='*15)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*15)
print('Total de pessoas com mais de 18 anos {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(totH))
print('E temos {} mulheres com menos de 20 anos'.format(totM20))

