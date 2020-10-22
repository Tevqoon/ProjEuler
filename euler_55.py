def palindromep(n):
    return n == int(str(n)[::-1])

def make_palindrome(n, c=1):
    x = n + int(str(n)[::-1])
    if c > 50:
        return False
    if palindromep(x):
        return (x, c)
    else:
        return make_palindrome(x, c=c+1)

c = 0
for i in range(1,10001):
    if not(make_palindrome(i)):
        c += 1

print(c)