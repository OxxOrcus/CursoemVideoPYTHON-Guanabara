dias = int(input('Quantos dias de locacao? '))
km = int(input('Quantos Km rodados? '))
custod = dias * 60
custokm = km * 0.15
total = custod + custokm
print('Valor total para {} dias e de R${:.2f} \nValor total para {}Km e de R${:.2f} \nValor total: R${:.2f}'.format(dias, custod, km, custokm, total))
