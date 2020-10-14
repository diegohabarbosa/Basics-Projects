#GAME Jokenpô: Pedra Papel e Tesoura
import random
from time import sleep
print('Jokenpô...')
print(' '*20)
sleep(2)
m = random.choice(['Pedra', 'Papel', 'Tesoura'])
v = str(input('Escolha entre Pedra, Papel e Tesoura: ')).strip().title()
print(' '*20)
print('Máquina escolheu {} e você escolheu {}'.format(m,v))
if m == 'Papel' and v == 'Pedra' or m == 'Tesoura' and v == 'Papel' or m == 'Pedra' and v == 'Tesoura':
    print('Você perdeu!!! Tente novamente...')
elif v == 'Papel' and m == 'Pedra' or v == 'Tesoura' and m == 'Papel' or v == 'Pedra' and m == 'Tesoura':
    print('Parabéns!!! Você ganhou...')
else:
    print('Deu empate!!! Tente novamente...')