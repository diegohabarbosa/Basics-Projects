#Condições Aninhadas
nome = str(input('Qual é o seu nome? '))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'João' or nome ==  'Maria' or nome == 'Ana':
    print('Sue nome é bem popular no Brasil.')
elif  nome in 'Juliana Camila Regina Tatiane':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
