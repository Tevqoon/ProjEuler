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

def rotations(s):
    s = str(s)
    return set(map(int ,{s[x:]+s[:x] for x in range(len(s))}))

circ_primes = []
for i in range(3, 10 ** 6):
    if is_prime(i):
        if len(list(filter(None, map(is_prime, rotations(i))))) == len(rotations(i)):
            circ_primes.append(i)

print(circ_primes)
print(len(circ_primes))

        