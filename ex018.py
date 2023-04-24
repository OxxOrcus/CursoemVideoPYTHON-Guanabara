from math import cos, sin, tan, radians
num = float(input('Digite um angulo: '))
s = sin(radians(num))
c = cos(radians(num))
t = tan(radians(num))
print('O seno deste angulo e {:.2f}\n'
      'O coseno deste angulo e: {:.2f}\n'
      'A tangente deste angulo e: {:.2f}\n'.format(s, c, t))
