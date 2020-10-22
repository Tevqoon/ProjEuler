import time

start = time.time()

def memo(fun):
    rezultati = {}
    def mem_f(x, y):
        if (x, y) not in rezultati:
            rez = fun(x, y)
            rezultati[(x, y)] = rez
            rezultati[(y, x)] = rez
        return rezultati[(x, y)]
    return mem_f

def mem(fun):
    rezultati = {}
    def mem_f(x):
        if (x) not in rezultati:
            rez = fun(x)
            rezultati[(x)] = rez
            rezultati[(x)] = rez
        return rezultati[(x)]
    return mem_f

@mem
def primep(x):
    if x == 1:
        return False
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(x ** (1 / 2) + 1), 2):
            if x % i == 0:
                return False
        else:
            return True

primes = [i for i in range(10000) if primep(i)]

def conc(a, b):
    return int(str(a) + str(b))

@memo
def conctest(a, b):
    return primep(conc(a, b)) and primep(conc(b, a))

print("starting loop")
primesets = []
for a in primes:
    for b in [i for i in primes if i > a and conctest(a, i)]:
        for c in [i for i in primes if i > b and conctest(a, i) and conctest(b, i)]:
            for d in [i for i in primes if i > c and conctest(a, i) and conctest(b, i) and conctest(c, i)]:
                for e in [i for i in primes if i > d and conctest(a, i) and conctest(b, i) and conctest(c, i) and conctest(d, i)]:
                    primesets.append([a,b,c,d,e])

end = time.time()
print(primesets)
print(sum(primesets[0]))
print("time elapsed: " + str(end - start) + "s")

#26033