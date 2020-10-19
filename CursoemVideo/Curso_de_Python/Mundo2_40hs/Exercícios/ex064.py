#064 - Tratando vários valores v1.0
b = c = s = 0
print('Digite os números inteiros, caso queira encerrar digite [999]!')
while s != 999:
    s = int(input('Digite um número inteiro: '))
    b += s 
    c += 1
print('A soma total foi de {} e foi digitado {} vezes.'.format(b-999,c-1))