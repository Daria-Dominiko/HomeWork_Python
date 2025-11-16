def month_to_season(month_number):
    if 1 <= month_number <=2 or month_number == 12:
        return "Зима"
    elif 3 <= month_number <= 5:
        return "Весна"
    elif 6 <= month_number <= 8:
        return "Лето"
    elif 9 <= month_number <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"

try:
    month_number = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month_number))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")