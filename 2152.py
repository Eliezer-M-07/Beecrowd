x = int(input())

for i in range(x):
    y = input().split(' ')

    H = y[0]
    M = y[1]
    O = y[2]

    if len(H) == 1:
        H = "0" + H
   

    if len(M) == 1:
        M = "0" + M



    if O == "1":
         print('{}:{} - A porta abriu!'.format(H,M))
    else:
        print('{}:{} - A porta fechou!'.format(H,M))
    
  
          

