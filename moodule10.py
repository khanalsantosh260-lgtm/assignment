#1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


# Test
if __name__ == "__main__":
    h = Elevator(1, 10)
    h.go_to_floor(5)
    h.go_to_floor(1)

#2
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)


# Test
if __name__ == "__main__":
    b = Building(1, 10, 3)
    b.run_elevator(0, 7)
    b.run_elevator(1, 3)

#3
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n🔥 Fire alarm activated! Moving all elevators to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)


# Test
if __name__ == "__main__":
    b = Building(1, 10, 3)
    b.run_elevator(0, 8)
    b.run_elevator(1, 5)
    b.fire_alarm()

#4
import random

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def drive(self, hours):
        self.distance += self.speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = max(0, min(car.max_speed, car.speed + change))
            car.drive(1)

    def print_status(self):
        print("\nCar\tSpeed\tDistance")
        for car in self.cars:
            print(f"{car.reg}\t{car.speed}\t{car.distance:.1f}")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)


# Main program
if __name__ == "__main__":
    cars = []
    for i in range(10):
        cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        if hours % 10 == 0:
            print(f"\n--- Hour {hours} ---")
            race.print_status()

    print("\n🏁 Race finished!")
    race.print_status() 