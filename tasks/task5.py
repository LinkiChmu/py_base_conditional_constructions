"""
Дана переменная, в которой хранится шестизначное число (номер проездного билета).
Программа определяет, является ли данный билет "счастливым".
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.
"""
number = 123456
first_3_digits = number // 1000
last_3_digits = number % 1000

digit_3 = first_3_digits % 10
digit_2 = (first_3_digits // 10) % 10
digit_1 = first_3_digits // 100
sum_first = digit_1 + digit_2 + digit_3

digit_6 = last_3_digits % 10
digit_5 = (last_3_digits // 10) % 10
digit_4 = last_3_digits // 100
sum_last = digit_4 + digit_5 + digit_6

if sum_last == sum_first:
    print("Счастливый билет")
else:
    print("Несчастливый билет")
