alu = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km rodados? '))
pda = 60 * alu
pkr = 0.15 * km
vap = pda + pkr
print('O valor a pagar é R$ {:.2f}'.format(vap))

#ou pago = ( dias * 60) + (km * 0.15)
