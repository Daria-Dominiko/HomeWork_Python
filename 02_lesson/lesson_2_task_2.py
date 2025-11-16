def dis_year_leap(number):
    return True if number % 4 == 0 else False

number = int(input("Введите число: "))
result = dis_year_leap(number)
print(f"Год {number}: {result}")