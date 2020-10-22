def triangle(n):
    return n * (n + 1) / 2

def pentagonalp(x):
    n = (1 + (1 + 24 * x) ** (1 / 2)) / 6
    return n == int(n)

def hexagonalp(x):
    n = (1 + (1 + 8 * x) ** (1 / 2)) / 4
    return n == int(n)

i = 286
while True:
    x = triangle(i)
    if pentagonalp(x):
        if hexagonalp(x):
            break
    i += 1
print(x)
