lst = []
for i in range(2, 1000000):
    digits = map(int, list(str(i)))
    if sum(map(lambda x: x ** 5, digits)) == i:
        lst.append(i)

print(lst)
print(sum(lst))

