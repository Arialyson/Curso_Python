preco = float(input('Qual o preço do produto? R$: '))
perc =  (preco*5/100)
desc = preco-perc
print('O seu produto com 5% de desconto é {:.2f}'.format(desc))
