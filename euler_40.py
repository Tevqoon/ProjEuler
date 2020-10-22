def champ(n):
    c = ""
    i = 1
    while len(c) <= n:
        c += str(i)
        i += 1
    return c

def d(n):
    return int(champ(n)[n - 1])

print(d(1) * d(10) * d(100) * d(1000) * d(100000) * d(1000000) * d(10000000))