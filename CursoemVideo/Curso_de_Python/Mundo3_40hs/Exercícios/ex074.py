#074 - Maior e menor valores em Tupla
from random import randint
valores = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
ordem = sorted(valores)
print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi {ordem[4]}')
print(f'O menor valor sorteado foi {ordem[0]}')
