def digits(n):
    return map(int, list(str(n)))

def dti(dgts):
    m = 0
    for n,i in enumerate(reversed(dgts)):
        m += i * 10 ** n
    return m

import itertools

products = set({})

for i in itertools.permutations(digits(123456789)):
    for x in range(1, 9):
        for y in range(x, 9):
            if dti(i[0:x]) * dti(i[x:y]) == dti(i[y:]):
                products.add(dti(i[y:]))

print(sum(products))
#products = {5346, 5796, 6952, 4396, 7852, 7632, 7254}
