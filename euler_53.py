def memo(fun):
    rezultati = {}
    def mem_f(x):
        if (x) not in rezultati:
            rezultati[(x)] = fun(x)
        return rezultati[(x)]
    return mem_f

#@memo
def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

def choose(n, r):
    return fact(n) // (fact(r) * fact(n - r))

n = 1
c = 0
while 1 <= n <= 100:
    for r in range(0, n + 1):
        print(n, r)
        c += 1 if choose(n, r) > 1000000 else 0
    n += 1

print(c)