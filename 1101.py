while True:
    m,n = input().split(' ')
    m = int(m)
    n = int(n)
    s = 0

    if m <= 0 or n <= 0:
        break

   
    if n > m:
        for i in range(m,n+1):
            s += i
            print(i,end=' ')
        print('Sum={}'.format(s))

    elif n < m:
        for i in range(n,m+1):
            s += i
            print(i,end=' ')
        print('Sum={}'.format(s))

    
