#EXERCICIO017 CAUCULE A HIPOTENUSA
'''
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hipo = (cato ** 2 + cata ** 2) ** (1/2)
print('O comprimento da hipotenusa e: {:.2f}'.format(hipo))
'''

from math import hypot
cato = float(input('Digite o compreimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(cato, cata)
print('O resuntado e: {:.2f}'.format(hipo))

