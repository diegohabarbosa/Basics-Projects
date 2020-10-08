#conversor de moedas
a = float(input('Quanto em Reais você tem na sua carteira? R$'))
b = float(a/5.56)
print('Com R${:.2f} você pode comprar US${:.2f} doláres'.format(a,b))