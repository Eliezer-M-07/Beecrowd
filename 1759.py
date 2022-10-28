n = int(input())

h = []
while n != 0:
    h.append('Ho')
    n -= 1

h[-1] = 'Ho!'
print(' '.join(h))
