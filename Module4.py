#Module 4
#1
#for n in range(3, 1001, 3):
   # print(n)
#2
# inches = float(input("Enter inches: "))
# while inches>0:
#     cm=inches * 2.54
#     print(cm)
#     inches=float(input("Enter inches: "))
#     if inches<0:
#         break
#3
# smallest = None
# largest = None
# number = input("Enter a number (empty to stop): ")
# while number != "":
#     number = float(number)
#     if smallest is None or number < smallest:
#         smallest = number
#     if largest is None or number > largest:
#         largest = number
#         number = input("Enter a number (empty to stop): ")
# if smallest is None:
#     print("No numbers entered.")
# else:
#     print("Smallest: " + str(smallest))
#     print("Largest: " + str(largest))
#4
# import random
# secret = random.randint(1, 10)
# guess = int(input("Guess a number (1-10): "))
# while guess != secret:
#     if guess < secret:
#         print("Too low")
#     else:
#         print("Too high")
#     guess = int(input("Guess a number (1-10): "))
# print("Correct")
#5
# CORRECT_USER = "aaa"
# CORRECT_PASS = "bbb"
# attempts = 0
# MAX_ATTEMPTS = 5
# while attempts < MAX_ATTEMPTS:
#     username = input("Username: ")
#     password = input("Password: ")
#     if username == CORRECT_USER and password == CORRECT_PASS:
#         print("Welcome")
#         break
#     else:
#         attempts = attempts + 1
#         print("Incorrect. Attempts left: " + str(MAX_ATTEMPTS - attempts))
# if attempts == MAX_ATTEMPTS:
#     print("Access denied")
#6
# import random
# N = int(input("How many random points to generate? "))
# inside_circle = 0
# i = 0
# while i < N:
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x * x + y * y < 1:
#         inside_circle = inside_circle + 1
#     i = i + 1
# pi = 4.0 * inside_circle / N
# print("Number of points generated:", N)
# print("Points inside circle:", inside_circle)

# print("Approximation of pi:", pi)