"""
Multiplicate two numbers using FFT algorithm

Input: Numbers a,b 
Output: Number a*b (in time O(n*log(n)))

Algorithm:
- create poly with coeffs a_0,a_1,...,a_n
- get evaluated values of complex guys x_0,x_1,...,x_n 

- same for b_0,...,b_n
- get values y_0,...,y_n

- get z_0,...,z_n = (x_0 * y_0, ... , x_n * y_n)

- use inverse fourier transform to get koefficients c0,...,c_n

FFT Algorithm:
- create list of primitive roots 
- split my coefficients into even and odd
- recursively evaluate

"""

import math

def find_padding_length(a : int, b : int) -> int:
    return 2**math.ceil(math.log2(max(len(str(a)),len(str(b)))*2))

def create_poly(num : int, len_padding : int) -> list[complex]:
    unpadded = [int(ch) for ch in str(num)]
    return [complex(x) for x in list(list(reversed(unpadded)) + (len_padding - len(unpadded)) * [0])]

def fft(a : list[complex], omegas: list[complex]) -> list[complex]:
    
    if len(a) == 1:
        return a

    even = a[::2]
    odd = a[1::2]
    
    x = fft(even,omegas[::2])
    y = fft(odd,omegas[::2])

    z = []

    for i in range(len(x)):
        z.append(x[i] + omegas[i] * y[i])

    for i in range(len(x)):
        z.append(x[i] - omegas[i] * y[i])
    
    return z

def get_z_evals(x : list[complex], y : list[complex]) -> list[complex]:
    return [xi * yi for (xi,yi) in zip(x,y)]

def get_number_from_z_evals(z : list[complex]) -> int:
    res = 0
    while round(z[-1].real) == 0:
        z.pop()
    for i in range(len(z)-1,-1,-1):
        res *= 10
        res += round(z[i].real)
    return res

def mult(k : int, l : int) -> int:

    padding_l = find_padding_length(k,l)

    a = create_poly(k,padding_l)
    b = create_poly(l,padding_l)

    # print([round(x.real) for x in a])
    # print([round(x.real) for x in b])

    n = max(len(a),len(b))

    theta = 2 * math.pi / n
    omegas = [complex(math.cos(i*theta),math.sin(i*theta)) for i in range(n)]
    
    x = fft(a,omegas)
    y = fft(b,omegas)

    z = get_z_evals(x,y)

    r = [1/n * x for x in fft(z,[o.conjugate() for o in omegas])]

    # print([round(x.real) for x in r])

    return get_number_from_z_evals(r)

a = 3423459304850943850938590384589403
b = 234390485394058039485

print(f"{a} * {b} = {a*b}")
print(f"{a} * {b} = {mult(a,b)}")
