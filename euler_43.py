from itertools import permutations

def num(perm):
    n = ""
    for i in perm:
        n += str(i)
    return int(n)

def prop(n):
    s = str(n)
    return int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0 and int(s[3:6]) % 5 == 0 and int(s[4:7]) % 7 == 0 and int(s[5:8]) % 11 == 0 and int(s[6:9]) % 13 == 0 and int(s[7:10]) % 17 == 0

numbers = []
for i in permutations(range(10)):
    if prop(num(i)):
        numbers.append(num(i))

print(numbers)
print(sum(numbers))