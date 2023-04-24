n1 = float(input('Escolha um numero: '))
n2 = float(input('Escolha outro numero: '))
result = n1 + n2
print('A soma e: {}'.format(result))


# OPERADORES ARITIMETICOS

5 + 2 # 7 Soma
5 - 2 # 3 Subtracao
5 * 2 # 10 Multiplicacao
5 / 2 # 2.5 Divisao

5 ** 2 # 25 Exponenciacao
5 // 2 # 2 Divisao inteira
5 % 2  # 1 Resto da Divisao
pow(4,3) # Potencia fora de ordem de precedencia
81 **(1/2) # 9 Raiz Quadrada
127**(1/3) # 5.026525695313479 Raiz Cubica

# ORDEM DE PRECEDENCIA

1 ()             #Primeira a ser realizada
2 **             #Segundo a ser realizada
3 * / // %       # resolver quem aparecer primeiro
4 + -            # por ultimo realizar soma e subtracao
