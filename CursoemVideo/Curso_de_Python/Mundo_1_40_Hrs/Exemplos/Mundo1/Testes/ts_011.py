# Cores no Terminal - PADRÃO ANSI
print('\033[0;30;41mTESTE')
print('\033[4;33;44mTESTE')
print('\033[1;35;43mTESTE')
print('\033[30;42mTESTE')
print('\033[mTESTE')
print('\033[7;30mTESTE')
print('\033[4;30;44mTESTE\033[m')
print('\033[7;37;44mTESTE\033[m')

#------------------------------------ Testando comandos -------------------------------------
a = 3
b = 5
print('Os valores são \033[7;37;44m{}\033[m'.format(a)+' e \033[1;30;43m{}\033[m'.format(b))

#--------------------------------------------------------------------------------------------
nome = input('Digite o seu nome: ')
print('Olá! Muito prazer em te conhecer {}{}{}'.format('\033[4;33m', nome, '\033[m'))
