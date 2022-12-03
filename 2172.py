while True:
    x = input().split(' ')

    if int(x[0]) == 0 and int(x[1]) == 0:
        break
    else:
        print(int(x[0]) * int(x[1]))
        
