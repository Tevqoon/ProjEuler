def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

perms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def perm_digits(m, lst):
    if len(lst) == 1:
        return str(lst[0])
    else: 
        x = len(lst) - 1
        val = m // fact(x)
        return str(lst.pop(val)) + perm_digits(m - val * fact(x), lst)

print(perm_digits(1000000 - 1, perms))
