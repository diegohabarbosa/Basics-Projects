#058 - Jogo da Adivinhação v2.0
import random
from time import sleep
t = 1
num = int(random.randint(0,5))
print('Pensei em número entre 0 à 10. Vamos ver se você consegue advinhar...')
user = int(input('Advinha qual número eu pensei entre 0 à 10? '))
while user != num:
    print('Infelizmente você errou! Tente novamente!')
    user = int(input('Advinha qual número eu pensei entre 0 à 10? '))
    if user != num:
        t += 1
    else:
        0
print('Eu pensei no número {} e você no número {}'.format(num, user))
print('Parabéns você acertou!!! Você precisou de {} tentativas para acertar.'.format(t))