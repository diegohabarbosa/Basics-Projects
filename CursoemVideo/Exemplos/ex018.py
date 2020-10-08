#Seno, Cosseno e Tangente
import math
an = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem o Seno de {:.2f}'.format(an,se))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an,co))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(an,tan))
