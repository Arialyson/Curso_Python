'''---------- por conceito matemático ------  '''

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Coprimento do cateto adjacente: '))
hi = ((co**2)+(ca**2))**(1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hi))'''

'''----------- importando a biblioteca ------ '''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))



