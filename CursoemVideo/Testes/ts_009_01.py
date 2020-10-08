"""
tempo = int(input('Quantos anos de uso tem o seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')
"""
tempo = int(input('Quantos anos de uso tem o seu carro? '))
print('Carro novo' if tempo<=3 else 'Carro Velho')
print('--FIM--')