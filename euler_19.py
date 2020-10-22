def je_prestopno(leto):
    if leto % 4 == 0:
        if leto % 100 == 0:
            if leto % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False

def stevilo_dni(mesec, leto):
    if mesec == 2:
        if je_prestopno(leto):
            return 29
        else:
            return 28
    if mesec <= 7:
        if mesec % 2 == 1:
            return 31
        else:
            return 30
    else:
        if mesec % 2 == 0:
            return 31
        else:
            return 30 

def days_in_a_year(year):
    return 366 if je_prestopno(year) else 365

def nth_day(day, month, year):
    count = 0
    for i in range(1, month):
        count += stevilo_dni(i, year)
    count += day
    return count

def nth_day_since_1900(day, month, year):
    count = 0
    for i in range(1900, year):
        count += days_in_a_year(i)
    count += nth_day(day, month, year)
    return count

count = 0
dates = [(month, year) for month in range(1,13) for year in range(1901, 2001)]

for i in dates:
    count += 1 if  nth_day_since_1900(1, i[0], i[1]) % 7 == 0 else 0

print(count)