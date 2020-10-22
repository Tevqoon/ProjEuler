from functools import reduce

def test(x):
    nums = map(str, [x * i for i in range(1, 7)])
    def same_letters(x, y):
        for i in x:
            if not(i in y):
                return y
        if len(x) != len(y):
            return y
        else:
            return x

    r = reduce(same_letters, nums)
    return r != str(x)

n = 1
while test(n):
    n += 1
print(n)