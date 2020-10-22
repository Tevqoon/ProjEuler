def memo(fun):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = fun(x)
        return rezultati[x]
    return mem_f

@memo
def is_prime(n):
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    for i in range(3, round(n ** (1 / 2)), 2):
        if n % i == 0:
            return False
    return True

def num_of_primes(a, b):
    n = 0
    while is_prime(abs(n ** 2 + a * n + b)):
        n += 1
    return n

mx_a_b = (0, 0)
mx = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        mx2 = max(mx, num_of_primes(a, b))
        if mx2 > mx:
            mx_a_b = (a, b)
            mx = mx2
print(mx_a_b)
print(mx_a_b[0] * mx_a_b[1])