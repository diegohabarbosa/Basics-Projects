# Analisando Triângulo
from time import sleep
r1 = float(input('Primeiro segmento: ')) 
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print(' '*25)
print('Aguarde enquanto analisamos os segmentos...')
print(' '*25)
sleep(3)
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')