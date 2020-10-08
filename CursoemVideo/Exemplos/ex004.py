# Dissecando uma variável
a = input('Digite algo: ')
b = type(a)
c = a.isdecimal()
d = a.isalpha()
e = a.isalnum()
print('O tipo primitivo de {0} é: {1} é um número? {2}, é um Alfa: {3}, é um Alfanumérico: {4}'.format(a,b,c,d,e))