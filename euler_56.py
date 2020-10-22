def d_sum(x):
    return sum(map(int, list(str(x))))

mx = 0
for a in range(100):
    for b in range(100):
        mx = max(mx, d_sum(a ** b))

print(mx)