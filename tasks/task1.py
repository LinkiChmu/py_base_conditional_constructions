"""
The program checks which of the entered strings is longer.

"""
phrase_1 = input("Введите фразу 1: ")
phrase_2 = input("Введите фразу 2: ")
if len(phrase_2) == len(phrase_1):
    print("Фразы равной длины")
elif len(phrase_2) > len(phrase_1):
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фраза 1 длиннее фразы 2")
