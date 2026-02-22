#1
import random
# def roll_d6():
#     return random.randint(1, 6)
# while True:
#     r = roll_d6()
#     print("Roll:", r)
#     if r == 6:
#         break

#2
# import random
# def roll_die(sides):
#     return random.randint(1, sides)
# sides = int(input("Enter number of sides: "))
# result = 0
# while result != sides:
#     result = roll_die(sides)
#     print("Roll:", result)

#3
# def gallons_to_liters(g):
#     return g * 3.78541
# while True:
#     g = float(input("Enter gallons (negative number to stop): "))
#     if g < 0:
#         print("Program ends.")
#         break
#     liters = gallons_to_liters(g)
#     print(g, "gallons =", liters, "liters")

#4
# def sum_list(numbers):
#     total = 0
#     for n in numbers:
#         total = total + n
#     return total
# data = [5, 8, 3, 7]
# result = sum_list(data)
# print("The sum of the list is", result)

#5
# def remove_odds(numbers):
#     result = []
#     for n in numbers:
#         if n % 2 == 0:
#             result.append(n)
#     return result
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# new_list = remove_odds(data)
# print("Original list:", data)
# print("Even numbers only:", new_list)

#6
# import math
# def unit_price(diameter, price):
#     radius = diameter / 2            # cm
#     radius_m = radius / 100          # convert cm → meters
#     area = math.pi * radius_m * radius_m   # m²
#     return price / area              # €/m²
#
# d1 = float(input("Enter diameter of pizza 1 (cm): "))
# p1 = float(input("Enter price of pizza 1 (€): "))
# d2 = float(input("Enter diameter of pizza 2 (cm): "))
# p2 = float(input("Enter price of pizza 2 (€): "))
# u1 = unit_price(d1, p1)
# u2 = unit_price(d2, p2)
# print("Pizza 1 unit price is", u1, "€/m²")
# print("Pizza 2 unit price is", u2, "€/m²")
# if u1 < u2:
#     print("Pizza 1 is better value")
# elif u2 < u1:
#     print("Pizza 2 is better value")
# else:
#     print("Both pizzas have the same value")