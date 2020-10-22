def prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    for i in range(3, round(n ** (1 / 2)), 2):
        if n % i == 0:
            return False
    return True

sequences = []
for i in range(1000, 10000 - 6660):
    if prime(i):
        if prime(i + 3330):
            if prime(i + 6660):
                for j in str(i):
                    if not(j in str(i + 3330) and j in str(i + 6660)): #doesn't weed out all the garbage
                        break
                    sequences += [[i, i + 3330, i + 6660]]
print(sequences)
#[2969, 6299, 9629]