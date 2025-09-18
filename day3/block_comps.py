"""
TODO: fix this
"""

a = [1]
max = 7

for n in range(0,max):
    a.append(0)
    a[n+1] = a[n]+sum([a[n-d-1] for d in range(3,n)])
    if n + 1 >= 3:
        a[n+1] += 1

print(a)