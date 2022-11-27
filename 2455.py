p1,c1,p2,c2 = input().split(' ')

s1 = int(p1) * int(c1)
s2 = int(p2) * int(c2)

if s1 == s2:
    print(0)
elif s1 < s2:
    print(1)
else:
    print(-1)
