p = int(input())
val = 0
for i in range(p):
    q = input().split(' ')
    qtd = int(q[1])

    if q[0] == '1001':
        val += qtd * 1.50
    if q[0] == '1002':
        val += qtd * 2.50
    if q[0] == '1003':
        val += qtd * 3.50
    if q[0] == '1004':
        val += qtd * 4.50
    if q[0] == '1005':
        val += qtd * 5.50

print('{:.2f}'.format(val))
