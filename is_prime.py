def is_prime(num):
    if num % num == 0 and num % 2 == 0:
        return True
    else:
        return False

num = int(input("Введите число: "))
print(is_prime(num))