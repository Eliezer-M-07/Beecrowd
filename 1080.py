l = []
for i in range(1,100+1):
    x = int(input())
    l.append(x) 

a = max(l)
print(a)
b = l.index(a)
print(b+1)
