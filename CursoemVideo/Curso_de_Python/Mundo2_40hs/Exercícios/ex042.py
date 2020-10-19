# Analisando Triângulo v2.0
from time import sleep
r1 = float(input('Primeiro segmento: ')) 
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print(' '*25)
print('Aguarde enquanto analisamos os segmentos...')
print(' '*25)
sleep(1)
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if r1 == r2 and r1 == r3:
        print('Este triângulo é um Equilátero')
    elif r1 == r2 and r1 !=  r3 or r1 == r3 and r1 != r2:
        print('Este triângulo é um Isósceles')
    else:
        print('Esse triânculo é um Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')