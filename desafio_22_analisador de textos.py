nome = str(input('Digite seu número completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {}'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

