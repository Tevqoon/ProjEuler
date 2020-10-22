def is_cube(x):
    return is_perfect(x, 3)

import math

def is_perfect(num, power):
    candidate = num ** (1/power)
    lo_candidate = int(math.floor(candidate))
    hi_candidate = int(math.ceil(candidate))
    return num == lo_candidate**power or num == hi_candidate**power

from itertools import permutations

def num(perm):
    n = ""
    for i in perm:
        n += str(i)
    return int(n)

def cube_perm(n):
    c = str(n ** 3)
    perms = set(permutations(c))
    return set(filter(is_cube, map(num, perms)))

def number_of_cube_perms(n):
    return len(cube_perm(n))

i = 0
while True:
    l = number_of_cube_perms(i)
    print(i, l)
    if l == 5:
        break
    i += 1
print(l)