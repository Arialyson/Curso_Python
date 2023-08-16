titulo = ' Conversor de médidas '
print('{:=^80}'.format(titulo))
medida = float(input('Digite uma distância em metro: '))
km = medida/1000
hm = medida/100
dam = medida/10
m = medida
dm = medida*10
cm = medida*100
mm = medida*1000
print('A médida de {}correspode a:')
print('{:.0f}km'.format(km))
print('{:.0f}hm'.format(hm))
print('{:.0f}dam'.format(dam))
print('{:.0f}m'.format(m))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))


