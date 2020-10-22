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

@memo
def prime_factors(n):
    if is_prime(n):
        return {n}
    else:
        for i in range(n):
            if is_prime(i):
                if n % i == 0:
                    return {i} | prime_factors(n // i)

n = 2
while True:
    if len(prime_factors(n)) == len(prime_factors(n + 1)) == len(prime_factors(n + 2)) == len(prime_factors(n + 3)) == 4:
        print(n)
        break
    n += 1