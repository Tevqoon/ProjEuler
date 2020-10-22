def memo(fun):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = fun(x)
        return rezultati[x]
    return mem_f

@memo
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    for i in range(3, round(n ** (1 / 2)), 2):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(10000) if is_prime(i)]

def goldbach(n):
    for p in primes:
        if p > n:
            return False
        else:
            for m in range( int(((n - p) / 2) ** (1 / 2)) + 1):
                if n == p + 2 * m ** 2:
                    return (p, m)
i = 3
while goldbach(i):
    i += 2
print(i) 