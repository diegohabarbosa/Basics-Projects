#068 - Jogo do Par ou Ímpar
from random import randint
v = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    maquina = randint(0,10)
    print('=-'*20)
    jogador = int(input('Diga um valor: '))
    total = jogador + maquina   
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {maquina}. Total de {total}', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você Venceu {v} vezes.')