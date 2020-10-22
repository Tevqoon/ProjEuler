import timeit

def prastevilo(n):
    for i in range(2, round(n ** (1 / 2))):
        if n % i == 0:
            return False
    return True

def prastevila(n):
    return list(filter(prastevilo, range(2, n)))

def timing():
    return prastevila(100)


def produkti(n, l):
    narray = list(str(n))
    produkti = [0 for i in range(len(narray) - l)]
    for i in range(len(narray) - l):
        produkt = 1
        for j in range(i, i + l):
            produkt *= int(narray[j])
        produkti[i] = produkt
    return max(produkti)

print(produkti(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 13))

def memo(fun):
    rezultati = {}
    def mem_f(x, y):
        if (x, y) not in rezultati:
            rezultati[(x, y)] = fun(x, y)
        return rezultati[(x, y)]
    return mem_f

def lattice_paths(size):
    @memo
    def lattice_path(x, y):
        print((x, y))
        if x == size or size == y:
            return 1
        else:
            return lattice_path(x + 1, y) + lattice_path(x, y + 1)
    return lattice_path(0, 0)
    
def number_word(n):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    numberstens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    numerals = list(map(int, list(str(n))))
    word = ""
    if len(numerals) == 1:
        return numbers[n]
    if len(numerals) == 3:
        word += numbers[numerals[0]] + "hundred"
    if len(numerals) == 3 and not(numerals[1] == 0 == numerals[2]):
        word += "and"
    if len(numerals) == 2 and 10 < n < 20:
        return numbers[n]
    if len(numerals) == 2:
        numerals = [0] + numerals
    if len(numerals) > 1 and not(numerals[1] == 0):
        word += numberstens[numerals[1]]
    if len(numerals) > 2 and not(numerals[2] == 0):
        word += numbers[numerals[2]]
    if n == 0:
        word = numerals[0]
    if n == 1000:
        word = "onethousand"
    return word

#print(list(map(number_word, range(1, 1001))))
#print(list(map(len, (map(number_word, range(1, 1001))))))

triangle = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

#some heuristics
sorted_triangle = list(map((lambda x: sorted(x, reverse=True)), triangle))
maximums = list(map(max, triangle))
th_best = sum(maximums)
average = sum(map(sum, triangle)) / (sum(map(len, triangle)))
average_path = average * len(triangle)

print(sorted_triangle)
print(maximums)
print(th_best)
print(average_path)

def triangle_max_sum(triangle):
    @memo
    def triangle_dynamic(v_x, v_y):
        if v_x == len(triangle) - 1:
            return triangle[v_x][v_y]
        else:
            return triangle[v_x][v_y] + max(triangle_dynamic(v_x + 1, v_y), 
                                            triangle_dynamic(v_x + 1, v_y + 1))
    return triangle_dynamic(0, 0)
