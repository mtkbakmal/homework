inputday = int(input("Введите день: "))
inputmonth = int(input("Введите месяц: "))
inputyear = int(input("Введите год: "))

def date(day, month, year):
    if day >= 1 and day <= 31 and month >= 1 and month <= 12 and year >= 0 and year <= 2026:
        return True
    else:
        return False

print(date(inputday, inputmonth, inputyear))
