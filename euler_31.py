coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
count = 0
 
for a in range(target, -1, -coins[7]):
    for b in range(a, -1, -coins[6]):
        for c in range(b, -1, -coins[5]):
            for d in range(c, -1, -coins[4]):
                for e in range(d, -1, -coins[3]):
                    for f in range(e, -1, -coins[2]):
                        for g in range(f, -1, -coins[1]):
                            count += 1

print(count)