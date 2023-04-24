
# SIMPLE print('The result is,', int(s))

# int sao numeros inteiros = 7, 12, -5, 1993
# float sao numeros reais 4.5, 0.075, 7.0
# bool sao 2 valores True e False
# str sao valores entre aspas 'Hello', '7', ' '
# BETTER print('The result is {}!'.format(s))

# print(type(n1)) para saber o tipo primitivo class

# COMPLEX OLD print('The result between', n1, 'and', n2, 'is:', int(s))
# abaixo o atual formato
print('The result between {} and {} is {}'.format(n1, n2, s))


n1 = int(input('Choice a number: '))
n2 = int(input('Choice a second number: '))
s = n1 + n2
print('The result between {} and {} is: {}'.format(n1, n2, s))
