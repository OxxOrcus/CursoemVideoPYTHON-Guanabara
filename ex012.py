#vn = float(input('Qual o valor do produto? R$'))
#vd = vn * (0.95)
#print('Seu valor com desconto e R${}!'.format(vd))

vn = float(input('Qual o valor do produto? R$'))
vd = vn - (vn * 5 / 100)
print('O valor com desconta e R${:.2f}'.format(vd))
