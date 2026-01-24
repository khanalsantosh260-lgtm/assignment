#Question 1
name = input("Santosh Khanal:")
print("Hello,"+ name+"!")

#question 2
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print("The area of the circle is:", area)

#question 3
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("Perimeter of the rectangle:", perimeter)
print("Area of the rectangle:", area)

#question 4
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
total = num1 + num2 + num3
product = num1 * num2 * num3
average = total / 3
print("Sum:", total)
print("Product:", product)
print("Average:", average)

#question 5
talent = int(input("Enter talents: "))
pound = int(input("Enter pounds: "))
lot = int(input("Enter lots: "))
total_lot = talent * 20 * 32 + pound * 32 + lot
total_grams = total_lot * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("The weight is", kilograms, "kilograms and", grams, "grams.")

#question 6
import random
code1 = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
code2 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
print("Three-digit lock code:", code1[0], code1[1], code1[2])
print("Four-digit lock code:", code2[0], code2[1], code2[2], code2[3])
