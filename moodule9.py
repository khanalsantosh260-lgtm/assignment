#1
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


# Main program
car = Car("ABC-123", 142)

print("Registration:", car.registration_number)
print("Maximum speed:", car.max_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)


#2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0


# Main program
car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed:", car.current_speed)

car.accelerate(-200)
print("Final speed after brake:", car.current_speed)

#3
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours



car = Car("ABC-123", 142)
car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)

print("Travelled distance:", car.travelled_distance)

#4
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Create cars
cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

# Race loop
finished = False

while not finished:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            finished = True

# Print results
print(f"{'Reg':<8} {'Max':<8} {'Speed':<8} {'Distance':<10}")
for car in cars:
    print(f"{car.registration_number:<8} "
          f"{car.max_speed:<8} "
          f"{car.current_speed:<8} "
          f"{car.travelled_distance:.2f}")