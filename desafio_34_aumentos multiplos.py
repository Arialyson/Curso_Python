salario = float(input('Qul é o sálario do funcionário? R$: '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
