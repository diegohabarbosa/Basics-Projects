#068 - Jogo do Par ou Ímpar
from random import randint
r = p = j = s = pi = v = g = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while r == pi:
    c = randint(0,10)
    print('=-'*20)
    j = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    s = c+j  
    if s%2 == 0:
        r = 'P'
    else:
        r = 'I'
    if r == pi:
        v += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    if r != pi:        
        print(f'Você jogou {j} e o computador {c}. Total de {s} DEU {r}')
        print('Você perdeu!')
        break
print(f'GAME OVER! Você Venceu {v} vezes.')