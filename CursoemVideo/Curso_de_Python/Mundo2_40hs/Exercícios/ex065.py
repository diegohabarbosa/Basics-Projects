#065 - Maior e Menor valores
resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant +=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print('Você digitou {} números e a média foi de {:.1f}'.format(quant, media))
print('O maior valor foi de {} e o menor foi de {}'.format(maior, menor))