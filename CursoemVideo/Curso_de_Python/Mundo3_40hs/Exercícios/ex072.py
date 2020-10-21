#072 - Número por Extenso
numero = int(input('Digite um número entre 0 e 20: '))
extenso = (0, 'Zero', 1, 'Um', 2, 'Dois', 3, 'Três', 4, 'Quatro', 5, 'Cinco', 6, 'Seis', 7, 'Sete', 8,  'Oito', 9, 'Nove', 10, 'Dez', 11, 'Onze', 12, 'Doze', 13, 'Treze', 14, 'Quatorze', 15, 'Quinze', 16, 'Dezesseis', 17, 'Dezessete', 18, 'Dezoito', 19, 'Dezenove', 20, 'Vinte')
posicao = len(extenso.index(numero+1))
print(f'Você digitou o número {extenso[posicao]}')