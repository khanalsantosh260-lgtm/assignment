#1
# import random
# n = int(input("How many dice to roll? "))
# total = 0
# for i in range(n):
#     roll = random.randint(1, 6)
#     total += roll
# print("Sum of dice:", total)

#2
# num = []
# while True:
#     s = input("Enter an integer (empty to stop): ")
#     if s == "":
#         break
#     nums.append(int(s))
# nums.sort(reverse=True)
# top_five = num[:5]
# print("Top five (desc):")
# for x in top_five:
#     print(x)

#3
# n = int(input("Enter an integer: "))
# if n <= 1:
#     print(n, "is not a prime number.")
# else:
#     is_prime = True
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             is_prime = False
#             break
#         d += 1
#     if is_prime:
#         print(n, "is a prime number.")
#     else:
#         print(n, "is not a prime number.")

#4
# cities = []
# for i in range(5):
#     name = input("Enter city " + str(i + 1) + ": ")
#     cities.append(name)
# print("You entered:")
# for city in cities:
#     print(city)