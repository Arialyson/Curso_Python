from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('categoria: MIRIM')
elif idade <= 14:
    print('categoria: INFANTIL')
elif idade <= 19:
    print('categoria: JUNIOR')
elif idade <= 25:
    print('categoria: SÊNIOR')
else:
    print('categoria: MASTER')
