def multiply(n):
    d = ""
    for i in range(1, 10):
        d += str(n * i)
    return int(d[:9])

def pandigital(n):
    s = str(n)
    d = "123456789"
    for i in d:
        if not(i in s):
            return False
    return True

mx = 0
for i in range(10000):
    m = multiply(i)
    if pandigital(m):
        mx = max(mx, m)
print(mx)