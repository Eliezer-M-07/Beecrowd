while True:
    try:
        l = int(input())
        v = input().split(' ')
        a = 0
        for i in range(l):

            if int(v[i]) > a:
                a = int(v[i])

        if a < 10:
            a = 1
        elif a >= 10 and a < 20:
            a = 2
        elif a >= 20:
            a = 3
        print(a)
      
    except EOFError:
        break
