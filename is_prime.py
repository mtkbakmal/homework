def is_prime(num):
    if num % num == 0 and num % 2 == 0:
        return True
    elif num > 1000:
        return "Превышающее значение."
    else:
        return False

num = int(input("Введите число: "))
print(is_prime(num))
