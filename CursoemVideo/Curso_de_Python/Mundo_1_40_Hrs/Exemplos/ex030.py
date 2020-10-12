# par ou impar?
n = int(input('Digite um número inteiro: '))
if (n%2) == 0:
    print('O número {} é '.format(n)+'\033[34m'+'PAR')
else:
    print('O número {} é '.format(n)+'\033[34m'+'ÍMPAR')