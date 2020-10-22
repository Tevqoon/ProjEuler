def intp(n):
    return n == int(n) and n > 0

def flatten(lists):
    ret = []
    for i in lists:
        for j in i:
            ret.append(j)
    return ret

def integral_length_sides(p):
    sides = []
    for a in range(2, int(p / 3), 2):
        b = (p ** 2 - 2 * a * p) / (2 * p - 2 * a)
        if intp(b):
            c = p - a - b
            if intp(c):
                f = flatten(sides)
                if not(a in f and b in f and c in f):
                    sides.append((a, b, c))
    return sides

mx = 0
mx_p = 0
for i in range(1, 1001):
    s = integral_length_sides(i)
    if mx < len(s):
        mx = len(s)
        mx_p = i
    
print(mx_p)
