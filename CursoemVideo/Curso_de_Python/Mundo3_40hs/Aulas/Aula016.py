'''
lanche = ('Hamburger','Suco','Pizza','Pudim','Batata Frita')
print('{:^30}'.format('# jeito 1 #'))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Vou comer para caramba!')
print('{:^30}'.format('# jeito 2 #'))
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Vou comer para caramba!')
print('')
print(sorted(lanche))
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
del(b)
c = a + b
print(c)