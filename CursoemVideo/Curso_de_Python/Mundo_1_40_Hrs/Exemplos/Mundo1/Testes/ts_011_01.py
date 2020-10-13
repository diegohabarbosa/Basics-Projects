# Cores utilizando dicionário
nome = input('Digite o seu nome: ')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;35m'}
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))