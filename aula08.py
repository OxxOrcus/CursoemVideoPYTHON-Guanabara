# import doce geral e tudo
# from doce import pudim especifico e limitado

#EXEMPLO
import math
#ceil
#floor
#trunc
#pow
#sqrt
#factorial

from math import sqrt

import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} e {}'.format(num + raiz))
#
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} e igual a {:.2f}'.format(num, math.ceil(raiz)))
#
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} e igual a {:.2f}'.format(num, floor(raiz)))
