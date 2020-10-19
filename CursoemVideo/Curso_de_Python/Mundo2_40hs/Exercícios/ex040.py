# Aquele clássico da Média
n1 = float(input('Digite a sua nota de Matemática: '))
n2 = float(input('Digite a sua nota de Português: '))
media = (n1 + n2) // 2
if media < 5.0:
    print('REPROVADO! Sua média foi de {:.1f} estude mais...'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO! Sua média foi de {:.1f} quase foi dessa vez...'.format(media))
else:
    print('APROVADO! Sua média foi de {:.1f} parabéns, continue assim...'.format(media))