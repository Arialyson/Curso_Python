n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 7.0:
    print('Parabéns, você foi aprovado')
elif media >= 5 and media < 7:
    print('Você está em recuperação')
elif media < 5.0:
    print('você foi reprovado')
