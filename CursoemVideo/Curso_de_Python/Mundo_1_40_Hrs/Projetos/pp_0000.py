a = int(input('Insira o número de aulas assistidas: '))
a1 = int(input('Insira o número de exercícios feitos: '))
b = (40*a)/60
b1 = int(117-a1)
c = int(23-a)
c1 = (23.21*a1)/60
d = (40*c)/60
d1 = (23.21*b1)/60
e1 = b + c1
f1 = d + d1
print('Você assistiu {} aulas que é equivalente à {:.2f} horas e ainda restam {} aulas que é equivalente há {:.2f} horas'.format(a,b,c,d))
print('Você fez um total de {} exercícios, ainda restam {} exercícios a serem feitos!'.format(a1,b1))
print('Você levou {:.2f} horas em exercícios feitos e provavelmente levará mais {:.2f} horas em exercícios'.format(c1,d1))
print('Você já estudou equivalente há {:.2f} horas e neste curso será investido um total de {:.2f} horas'.format(e1, f1))
