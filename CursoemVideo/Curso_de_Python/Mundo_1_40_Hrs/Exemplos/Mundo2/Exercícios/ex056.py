#056 - Analisador completo
hv = 0
mm = 0
ti = 0
for c in range(0,4):
    n = str(input('Digite o {}º nome: '.format(c+1))).strip().title()
    i = int(input('Digite a idade da {}ª pessoa: '.format(c+1)))
    s = str(input('Digite o sexo: [ F ] para Feminino e [ M ] Masculino: ')).strip().upper()
    ti += i
    if s == 'F' and i < 20:
        mm += 1
    elif s == 'M':
        if i > hv:
            hv = i
            nh = n
print('A média de idade do grupo é de {} anos'.format(ti/4))
print('No grupo há {} mulheres menores de 20 anos.'.format(mm))
print('O nome do homem mais velho do grupo é {} e ele tem {} anos'.format(nh,hv))