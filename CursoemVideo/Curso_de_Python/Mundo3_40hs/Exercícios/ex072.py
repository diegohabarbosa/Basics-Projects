#072 - Número por Extenso
numero = 'x'
conflito = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
while numero not in conflito:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ',end='')
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print(f'Você digitou o número {extenso[numero]}')
