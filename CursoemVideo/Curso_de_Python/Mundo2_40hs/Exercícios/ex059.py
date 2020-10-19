#059 - Criando um Menu de Opções
c = 4
while c == 4:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    print('--'*25)
    print('Digite [ 1 ] para somar')
    print('Digite [ 2 ] para multiplicar')
    print('Digite [ 3 ] para maior')
    print('Digite [ 4 ] para novos números')
    print('Digite [ 5 ] para sair do programa')
    print('--'*25)
    c = int(input('Qual opção você escolheu?: '))
    if c == 1:
        x = a+b
    elif c == 2:
        x = a*b
    elif c == 3:
        x = max(a,b)
    else:
        ''
print(x)
print('FIM!')