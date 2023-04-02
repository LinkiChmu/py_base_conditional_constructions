"""
The program for the selection of packages according to the size of the goods.
Dimensions (width, length, height) are stored in variables (in centimeters):
* if each of the three dimensions is less than or equal to 15 cm, displays "Box No.1";
* if at least one of the measurements is more than 2 m - "Ski package";
* if at least one of the measurements is more than 15 cm, but less than 50 cm - "Box No.2";
in all other cases - "Box No.3".

"""
width = 15
length = 55
height = 15

if width <= 15 and length <= 15 and height <= 15:
    print("Стандартная коробка №1")
elif width > 200 or length > 200 or height > 200:
    print("Ищите упаковку для лыж")
elif 15 < width < 50 or 15 < length < 50 or 15 < height < 50:
    print("Стандартная коробка №2")
else:
    print("Стандартная коробка №3")
