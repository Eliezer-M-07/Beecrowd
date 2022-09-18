x = int(input())
y = int(input())

nd = []

if x > y:
    for i in range(y,x+1):
        if i % 13 != 0:
            nd.append(i)

if x < y:
    for i in range(x,y+1):
        if i % 13 != 0:
            nd.append(i)
            
print(sum(nd))
