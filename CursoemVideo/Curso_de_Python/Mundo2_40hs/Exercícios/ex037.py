# Conversor de bases númericas
from time import sleep
numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
sleep(2)
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida. Tente novamente!')