def is_prime(num):
    if num <= 1:
        return False
    elif num > 1000:
        return "Превышающее значение."
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        return True

num = int(input("Введите число: "))
print(is_prime(num))
