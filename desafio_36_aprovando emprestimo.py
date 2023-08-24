casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa /(anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestímo pode ser CONCEDIDO!')
else:
    print('Emprestiímo NEGADO!')
