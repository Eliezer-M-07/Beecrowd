x = int(input())
qtd = 0

y = input().split(' ')

a = int(y[0])
b = int(y[1])
c = int(y[2])
d = int(y[3])
e = int(y[4])

if a == x:
    qtd+=1
if b == x:
    qtd+=1
if c == x:
    qtd+=1
if d == x:
    qtd+=1
if e == x:
    qtd+=1

print(qtd)
