# calculando descontos
a = float(input('Digite o preço do produto:'))
b = a*0.95
c = a - (a*5/100)
print('O preço do produto é R$ {:.2f} com 5% de desconto vai para R$ {:.2f}'.format(a,b))
print('O preço do produto é R$ {:.2f} com 5% de desconto vai para R$ {:.2f}'.format(a,c))
