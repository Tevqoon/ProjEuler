## Te sem naredil nekaj let nazaj, prilagam le na hitro spisane funkcije.

def euler_1(n):
    nums = []
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            nums.append(i)
    return sum(nums)

print("1: " + str(euler_1(1000)))

def euler_2(n):
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    f = fib()
    s = 0
    for x in f:
        if x % 2 == 0:
            s += x
        if x >= n:
            break
    return s

print("2: " + str(euler_2(4000000)))

def is_prime(p):
    for i in range(2, int(p ** (1 / 2)) + 1):
        if p % i == 0:
            return False
    return True

def euler_3(n):
    for i in range(int(n ** (1 / 2)) - 1, 0, -2):
        if is_prime(i) and n % i == 0:
            return i
    return n

#print("3: " + str(euler_3(600851475143)))

def euler_4():
    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    current = 0
    x = 100
    while x <= 999:
        y = x
        while y <= 999:
            if is_palindrome(x * y):
                current = max(current, x * y)
            if x * y <= current:
                break
            y += 1
        x += 1
    return current

print("4: " + str(euler_4()))

def euler_5():
    primes = filter(is_prime, range(1, 21))
    m = 1
    for i in primes:
        m *= i
    # calculated the divisors of the rest by hand
    return (2 ** 3) * 3 * m

print("5: " + str(euler_5()))

def euler_6():
    return (sum(range(1, 101)) ** 2) - sum([i ** 2 for i in range(1, 101)])

print("6: " + str(euler_6()))

def euler_7():
    index = 0
    p = 2
    while index < 10001:
        if is_prime(p):
            index += 1
        p += 1
    return p - 1

print("7: " + str(euler_7()))

def euler_8(n, l):
    narray = list(str(n))
    produkti = [0 for i in range(len(narray) - l)]
    for i in range(len(narray) - l):
        produkt = 1
        for j in range(i, i + l):
            produkt *= int(narray[j])
        produkti[i] = produkt
    return max(produkti)

print("8: " + str(euler_8(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 13)))

def euler_9():
    a = 3
    while True:
        for b in range(a, 1000 - a):
            c = (a * a + b * b) ** (1 / 2)
            if a + b + c == 1000:
                if c == int(c):
                    return int(a * b * c)
        a += 1

print("9: " + str(euler_9()))
    
def euler_10():
    s = 2
    for i in range(3, 2 * 10 ** 6 + 1, 2):
        if is_prime(i):
            s += i
    return(s)

print("10: " + str(euler_10()))