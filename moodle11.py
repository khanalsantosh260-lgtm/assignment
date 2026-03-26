#1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine name: {self.name}")
        print(f"Chief editor: {self.chief_editor}")


# Main program
magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
print()
book.print_information()

#2
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance_traveled = self.distance_traveled + self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


# Main program
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(120)
gasoline_car.accelerate(100)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"{electric_car.registration_number}: {electric_car.distance_traveled} km")
print(f"{gasoline_car.registration_number}: {gasoline_car.distance_traveled} km")