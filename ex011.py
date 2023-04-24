larg = float(input('Qual a Largura da parede? '))
alt = float(input('Qual a Altura da parede? '))
area = larg * alt
litros = area / 2
print('Sua parede tem {:.1f}m\nVoce ira precisar de {:.1f}l de tinta!'.format(area, litros))
