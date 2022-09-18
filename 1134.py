# -*- coding: utf-8 -*-

a = 0
g = 0
d = 0

while True:
    c = int(input())
    if c == 1:
        a +=1
    if c == 2:
        g +=1
    if c == 3:
        d+=1
    if c == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))
