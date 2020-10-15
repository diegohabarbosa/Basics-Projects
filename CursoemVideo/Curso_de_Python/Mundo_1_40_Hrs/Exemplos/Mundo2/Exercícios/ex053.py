#053 - Detector de Palíndromo
for c in range(0,1):
    f = input('Insira uma frase para idenficar se é um Palíndromo: ').strip()
    fr = format(f.replace(' ','')).upper()
    rf = fr[::-1]
    if fr == rf:
        print('Essa frase é um Palíndromo')
    else:
        print('Essa frase não é um Palíndromo')