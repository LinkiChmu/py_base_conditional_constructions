"""
Given a variable that stores a six-digit number (ticket number).
The program determines if the given ticket is "lucky".
A ticket is considered lucky if the sum of the first three digits matches
the sum of the last three digits of the number.
"""
number = 123345

digit_1 = number // (10**5)
digit_3 = number // (10**4) % 10
digit_2 = number // (10**3) % 10
digit_4 = number // (10**2) % 10
digit_5 = number // 10 % 10
digit_6 = number % 10

sum_first = digit_1 + digit_2 + digit_3
sum_last = digit_4 + digit_5 + digit_6

print("Счастливый билет") if sum_last == sum_first else print("Несчастливый билет")
