"""
The program displays whether the entered year is a leap year or a common year.

"""
year = int(input("Введите год в формате 'yyyy':\n"))
print("Високосный год" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
      else "Обычный год")
