# Jogo da adivinhação
import random
num = int(random.randint(0,5))
print('Pensei em número entre 0 à 5. Vamos ver se você consegue advinhar')
user = int(input('Advinha qual número eu pensei entre 0 à 5? '))
print('Eu pensei no número {} e você no número {}'.format(num, user))
if user == num:
    print('PARABÉNS você acertou!!!')
else:
    print('Infelizmente você errou! Tente novamente!')
#print('PARABÉNS você acertou!!!' if user == num else 'Infelizmente você errou! Tente novamente!')
#if user >5: print('É para advinhar entre 0 e 5 BURRO! Tente novamante!')