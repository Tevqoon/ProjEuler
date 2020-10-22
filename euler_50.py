def memo(fun):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = fun(x)
        return rezultati[x]
    return mem_f

@memo
def je_prastevilo(n):
    if n == 1:
        return False
    for i in range(2, round(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

print("making primelist...")
primes = [i for i in range(1, 1000000) if je_prastevilo(i)]
print("done")

print("starting seeking")
primesum = 0
number = 0
for i in range(0, len(primes)):
    j = i
    n = 0
    print(j)
    s = 0
    sn = 0
    while sn < 1000000 and j < len(primes):
        sn = s + primes[j]
        n += 1
        if sn > 1000000:
            break
        else:
            s = sn
        j += 1
        if je_prastevilo(s) and n > number:
            primesum = s
            number = n


print(primesum, number)
        
