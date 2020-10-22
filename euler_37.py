def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    for i in range(3, round(n ** (1 / 2) + 1), 2):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(p):
    s = str(p)
    for i in range(len(s)):
        if not(is_prime(int(s[i:]))):
            return False
    if p in [2,3,5,7]:
        return False
    return True

def right_truncatable_prime(p):
    s = str(p)
    for i in range(len(s)):
        if not(is_prime(int(s[:len(s) - i]))):
            return False
    if p in [2,3,5,7]:
        return False
    return True

def double_truncatable_prime(p):
    return left_truncatable_prime(p) and right_truncatable_prime(p)

dtps = []
i = 2
while len(dtps) < 11:
    if double_truncatable_prime(i):
        dtps.append(i)
    i += 1

print(dtps)
print(sum(dtps))