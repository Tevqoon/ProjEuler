from itertools import permutations

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    for i in range(3, round(n ** (1 / 2) + 1), 2):
        if n % i == 0:
            return False
    return True

def num(perm):
    n = ""
    for i in perm:
        n += str(i)
    return int(n)

for i in range(9, 0, -1):
    for p in list(permutations(range(i, 0, -1))):
        if is_prime(num(p)):
            print(num(p))
            break