def primep(x):
    if x == 1:
        return False
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(x ** (1 / 2) + 1)):
            if x % i == 0:
                return False
        else:
            return True

def lti(l):
    s = ""
    for i in l:
        s += str(i)
    return int(s)

def num_replace_2(x):
    digits = list(map(int, str(x)))
    nums=[]
    for i in range(len(digits)):
        for j in range(len(digits)):
            if i != j:
                for d in range(10):
                    digits2 = digits.copy()
                    digits2[i] = d
                    digits2[j] = d 
                    nums.append(digits2)
    nums = map(lti, nums)
    return groupby(nums, 9)

def num_replace_3(x):
    digits = list(map(int, str(x)))
    nums=[]
    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):
                if i != j != k and i != k:
                    for d in range(10):
                        digits2 = digits.copy()
                        digits2[i] = d
                        digits2[j] = d 
                        digits2[k] = d
                        nums.append(digits2)
    nums = map(lti, nums)
    return groupby(nums, 9)

def groupby(lst, x):
    newlst = []
    c = 0
    tmplst = []
    for i in lst:
        tmplst.append(i)
        if c == x:
            c = 0
            newlst.append(tmplst)
            tmplst = []
        else:
            c += 1
    return newlst

def num_of_primes(lst):
    return len(list(filter(primep, lst)))

lst = []
i = 1210000
while True:
    if primep(i)
    print(i)
    if 8 in map(num_of_primes, num_replace_2(i)):
        lst.append(i)
        break
    i += 1
    if i > 2000000:
        break
print(lst)
