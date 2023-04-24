'''num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porcao inteira e {:.0f}'.format(num, num))'''

from math import trunc
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porcao inteira e {}'.format(num, '''int'''trunc(num)))