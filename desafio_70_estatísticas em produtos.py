total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = int(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont ==  1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa!'))
print(f'o total da compra foi R${total:.2f} Reais')
print('temos {} produtos custando mais de R$1000.00 reais'.format(totmil))
print('o produto mais barato foi {} que custa R${:.2f} reais'.format(barato, menor))
