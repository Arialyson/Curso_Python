peso = float(input('Qual é o seu peso?(Kg): '))
altura = float(input('Qual é a sua altura?(m): '))
imc = peso / altura **2
print('seu IMC é de {:.1f}Kg/m²'.format(imc))
print('-='*10)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc <30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
print('-='*10)
