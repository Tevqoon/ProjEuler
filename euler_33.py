def digits(n):
    return list(map(int, list(str(n))))

def simplified(a, b):
    da = digits(a)
    db = digits(b)
    for i in da:
        if i in db:
            da.remove(i)
            db.remove(i)
            return a / b == da[0] / db[0]
    return False

fractions = []
for i in range(10, 100):
    for j in range(10, 100):
        if not(0 in digits(i) or 0 in digits(j)) and i != j and i / j < 1:
            if simplified(i, j):
                fractions.append((i, j))

print(fractions)
#[(16, 64), (19, 95), (26, 65), (49, 98)]
print(16 * 19 * 26 * 49)
print(64 * 95 * 65 * 98)