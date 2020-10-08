# Analisador de textos

# Diego Henrique de Almeida Barbosa
# Tatiane Caroline Rocha
# Enzo Rocha Barbosa
nome = input('Digite o seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print(len(nome))
print('Seu nome tem ao todo {} letas'.format(len(nome.replace(' ',''))))
print('Seu primeiro nome é {} e ele tem um total de {} letras'.format(nome.split()[0],len(nome.split()[0])))
