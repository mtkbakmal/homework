inputday = int(input("Введите день: "))
inputmonth = int(input("Введите месяц: "))
inputyear = int(input("Введите год: "))

def date(day, month, year):
    if 1 == day <= 31 and 1 == month <= 12 and 0 == year <= 2026:
        return True
    else:
        return False

print(date(inputday, inputmonth, inputyear))