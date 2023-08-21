salario = float(input('Qual é o salário do funcionario? R$: '))
aumento = salario + (salario*15/100)
print('Um funcionário que ganhava R${:.2f}'.format(salario))
print('Com 15% de aumento passará a receber R${:.2f}'.format(aumento))

