x = input().split(' ')

h = int(x[0])
z = int(x[1])
l = int(x[2])

if h > l and h < z or h < l and h > z:
    print('huguinho')
elif l > h and l < z or l < h and l > z:
    print('luisinho')
else:
    print('zezinho')
