print('{:=^40}'.format(' Lojas Ariacanas '))
preço = float(input('Preço das compras R$:'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque (10% de desconto)
[2] à vista cartão (5% de desconto)
[3] 2x no cartão (sem juros)
[4] 3x ou mais no cartão (com acréscimo de 20%)''')
opção = int(input('Qual é a opção? '))
print('='*40)
if opção == 1:
    total = preço - (preço*10/100)
elif opção == 2:
    total = preço - (preço*5/100)
elif opção == 3:
    total = preço
    parcela = total /2
    print('sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço*20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. tente novamente!')
print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
