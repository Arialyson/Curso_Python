print('='*60)
larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
dime = larg*altu
tint = dime/2
print('Sua parede tem a área de {:.2f}m².\npara pintar essa parede, você precisará de {:.2f}l de tinta.'.format(dime, tint))
print('='*60)
