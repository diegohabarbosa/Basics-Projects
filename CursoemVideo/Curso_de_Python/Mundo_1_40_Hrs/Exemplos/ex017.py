#Catetos e Hipotenusa
from math import sqrt, hypot
#h² = ca² + co²
ca = float(input('Digite o valor de cateto: '))
ca2 = ca**2
co = float(input('Digite o valor de cateto oposto: '))
co2 = co**2
h2 = sqrt(ca2+co2)
hi = hypot(co, ca)
print('O valor da Hipotenusa é {:.2f}'.format(h2))
print('O valor da Hipotenusa é {:.2f}'.format(hi))
