"""
Программа запрашивает у пользователя месяц и дату рождения
и выводит соответствующий знак зодиака.
"""
born_day = int(input("Введите день:\n"))
if born_day < 0 or born_day > 31:
    print("Некорректный ввод числа\n")
else:
    month_input = input("Введите месяц:\n").lower()
    month = 0
    if month_input == "январь":
        month = 1
    elif month_input == "февраль":
        month = 2
    elif month_input == "март":
        month = 3
    elif month_input == "апрель":
        month = 4
    elif month_input == "май":
        month = 5
    elif month_input == "июнь":
        month = 6
    elif month_input == "июль":
        month = 7
    elif month_input == "август":
        month = 8
    elif month_input == "сентябрь":
        month = 9
    elif month_input == "октябрь":
        month = 10
    elif month_input == "ноябрь":
        month = 11
    elif month_input == "декабрь":
        month = 12
    else:
        print("Некорректный ввод месяца")

    if month != 0:
        # convert date of birth to integer format 'mmdd' or 'mdd'
        born_month_day = month * 100 + born_day
        if born_month_day < 121 or born_month_day > 1222:
            print("Ваш знак зодиака: Козерог")
        elif born_month_day < 220:
            print("Ваш знак зодиака: Водолей")
        elif born_month_day < 321:
            print("Ваш знак зодиака: Рыбы")
        elif born_month_day < 421:
            print("Ваш знак зодиака: Овен")
        elif born_month_day < 522:
            print("Ваш знак зодиака: Телец")
        elif born_month_day < 622:
            print("Ваш знак зодиака: Близнецы")
        elif born_month_day < 723:
            print("Ваш знак зодиака: Рак")
        elif born_month_day < 822:
            print("Ваш знак зодиака: Лев")
        elif born_month_day < 924:
            print("Ваш знак зодиака: Дева")
        elif born_month_day < 1024:
            print("Ваш знак зодиака: Весы")
        elif born_month_day < 1123:
            print("Ваш знак зодиака: Скорпион")
        elif born_month_day < 1223:
            print("Ваш знак зодиака: Стрелец")
