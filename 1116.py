x = int(input())

for i in range(x):
    y = input().split(' ')

    a = int(y[0])
    b = int(y[1])

    if b == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(a / b))
