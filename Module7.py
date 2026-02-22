#7
#1
# seasons = ("spring", "summer", "autumn", "winter")
# month = int(input("Enter month number (1-12): "))
# if month == 3 or month == 4 or month == 5:
#     print("Season:", seasons[0])   # spring
# elif month == 6 or month == 7 or month == 8:
#     print("Season:", seasons[1])   # summer
# elif month == 9 or month == 10 or month == 11:
#     print("Season:", seasons[2])   # autumn
# elif month == 12 or month == 1 or month == 2:
#     print("Season:", seasons[3])   # winter
# else:
#     print("Invalid month")
#2
# names = set()
# while True:
#     name = input("Enter a name (press Enter to stop): ")
#     if name == "":   # stop if empty
#         break
#     if name in names:
#         print("Existing name")
#     else:
#         print("New name")
#         names.add(name)
# print("Names you entered:")
# for n in names:
#     print(n)
#
#3
# Fetching and storing airport data
# Dictionary to store airports
# airports = {}
# while True:
#     print("\nChoose an option:")
#     print("1 = Enter a new airport")
#     print("2 = Fetch airport information")
#     print("3 = Quit")
#     choice = input("Your choice: ")
#     if choice == "1":
#         # Enter new airport
#         icao = input("Enter ICAO code (e.g., EFHK): ").upper()
#         name = input("Enter airport name: ")
#         airports[icao] = name
#         print("Airport saved!")
#     elif choice == "2":
#         icao = input("Enter ICAO code: ").upper()
#         if icao in airports:
#             print("Airport name:", airports[icao])
#         else:
#             print("Airport not found.")
#     elif choice == "3":
        # Quit program
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")
#
# #
#     else:
#         print("Invalid choice. Please select 1, 2, or 3.")

