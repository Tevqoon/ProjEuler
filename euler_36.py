def bin_dig(n):
    return str(bin(n))[2:]

def dbp(n):
    return str(n) == str(n)[::-1] and bin_dig(n) == bin_dig(n)[::-1]

db_palindromes = []
for i in range(1000000):
    if dbp(i):
        db_palindromes.append(i)

print(sum(db_palindromes))