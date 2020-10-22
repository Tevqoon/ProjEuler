def memo(fun):
    rezultati = {}
    def mem_f(x):
        if x not in rezultati:
            rezultati[x] = fun(x)
        return rezultati[x]
    return mem_f

@memo
def fibonacci(n):
    return 1 if n == 1 or n == 2 else fibonacci(n - 1) + fibonacci(n - 2)

i = 0
while True:
    i += 1
    x = fibonacci(i)
    if len(str(x)) >= 1000:
        break
print(i)
