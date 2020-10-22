def divisor(x):
    divisors = []
    for i in range(1, round(x / 2) + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

def is_abundant(x):
    return sum(divisor(x)) > x

abundant_numbers = []
for i in range(28123):
    if is_abundant(i):
        abundant_numbers.append(i)

sums_of_two_abundant_numbers = {i + j for i in abundant_numbers for j in abundant_numbers if i + j <= 28123}
all_numbers = {i for i in range(1, 28123 + 1)}

non_sum_numbers = all_numbers - sums_of_two_abundant_numbers
print(sum(non_sum_numbers))