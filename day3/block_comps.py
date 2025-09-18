"""
https://projecteuler.net/problem=114
"""

a = [1]
max = 50

for n in range(0,max+1):
    a.append(0)
    a[n+1] += a[n] # if n+1-th cell is an empty cell

    # d is not the full size of the brick but the amount of cells it covers from the n-celled area
    a[n+1] += sum([a[n-d-1] for d in range(2,n)]) # we have d cells taken from the full length of n+1 and also we have to leave one empty cell on the left of end of the brick
    if n + 1 >= 3:
        a[n+1] += 1 # we can also fit a full brick inside our designated area


print(a[max])