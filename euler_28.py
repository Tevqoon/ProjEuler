def spiral_diagonal_sum(n):
    spirals = [1]
    offset = 2
    i = 1
    while i <= n ** 2:
        for j in range(4):
            i += offset
            spirals.append(i)
        offset += 2
    return sum(spirals)

print(spiral_diagonal_sum(1000))
