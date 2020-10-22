def euclidean(a, b):
    retlist = []
    while not(a in map(lambda x: x[0], retlist)):
        n = a // b
        retlist.append((a, b, n))
        a = a % b * 10
    return retlist

def cycle(a, b):
    return list(map(lambda x: x[2],euclidean(a, b)))[1:]

def cycle_len(b):
    a = 10 % b
    l = 1
    while a != 1:
        a = a * 10 % b
        l += 1
    return l

def is_prime(n):
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    for i in range(3, round(n ** (1 / 2) + 1), 2):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(7, 1000):
    if is_prime(i):
        primes.append(i)

mx = 0
mx_p = 0
for i in range(len(primes)):
    print(i)
    t = cycle_len(primes[i])
    if mx < t:
        mx_p = primes[i]
        mx = t

print(mx_p)