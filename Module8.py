# 8
#1
# airports = {
#     "NP": "Tribhuvan International Airport, Kathmandu",
#     "FIN": "Helsinki-Vantaa Airport, Helsinki",
#     "UK": "Heathrow Airport, London",
# }
#
# # Ask the user
# code = input("Enter ICAO code: ").upper()
# if code in airports:
#     print("Airport info:", airports[code])
# else:
#     print("Airport not found")

 #2
# airports = [
#     ("FI", "Helsinki-Vantaa"),
#     ("FI", "Oulu"),
#     ("FI", "Turku"),
#     ("NP", "Tribhuvan"),
#     ("NP", "Pokhara"),
#     ("US", "Atlanta"),
#     ("US", "JFK"),
#     ("UK", "Heathrow"),
#     ("UK", "Gatwick")
# ]
#
# area = input("Enter area code (FI, NP, US, UK): ").upper()
# found = False
# for code, airport in airports:
#     if code == area:
#         if not found:
#             print("Airports in", area + ":")
#             found = True
#         print("-", airport)
#
# if not found:
#     print("No airports found for that area code")

#3
# from geopy.distance import geodesic
#
# # "Database": ICAO code -> (latitude, longitude)
# airports = {
#     "VNKT": (27.6966, 85.3591),   # Kathmandu
#     "DEL": (28.5562, 77.1000),    # Delhi
#     "DXB": (25.2532, 55.3657),    # Dubai
#     "DOH": (25.2736, 51.6081)     #  Doha
# }
# code1 = input("Enter first ICAO code: ").upper()
# code2 = input("Enter second ICAO code: ").upper()
# if code1 in airports and code2 in airports:
#     coords1 = airports[code1]
#     coords2 = airports[code2]
#
#     distance = geodesic(coords1, coords2).kilometers
#
#     print(f"Distance between {code1} and {code2} is {distance:.2f} km")
# else:
#     print("One or both airport codes not found.")
#
#
