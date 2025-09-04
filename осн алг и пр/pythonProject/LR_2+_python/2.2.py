# Напишите программу, вычисляющую по номеру месяца - целому числу от 1 до 12 - количество дней в месяце.
n_m = int(input("Введите номер месяцa: "))
if n_m < 8 and n_m % 2 != 0:
    print("31")
elif n_m == 2:
    print("28 or 29")
elif n_m < 8 and n_m % 2 == 0:
    print('30')
elif n_m >= 8 and n_m <= 12 and n_m % 2 == 0:
    print("31")
elif n_m >= 8 and n_m <= 12 and n_m % 2 != 0:
    print("30")
else:
    print("Такого месяца не существует")