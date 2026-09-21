class Vehicle:
    def start(self):
        print('Vehicle is starting')

class Car(Vehicle):
    pass

car1 = Car()
car1.start()


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

bike1 = Bike()
bike1.start()
bike1.ride()

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car engine is starting")

car1 = Car()
car1.start()


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike engine is ready")

bike1 = Bike()
bike1.start()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

bike1 = Bike("Honda", "Sport")

print(bike1.brand)
print(bike1.type)

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.brand}, {self.model}, {self.year} is starting")

    def display_info(self):
        print(f"{self.brand}")
        print(f"{self.model}")
        print(f"{self.year}")

    def update_year(self, new_year):
        self.year = new_year

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

    def start(self):
        super().start()
        print(f"{self.brand} {self.model} engine is starting")

car1 = Car("Toyota", "Camry", 2026)
car1.update_year(2026)
car1.display_info()
car1.start()
car1.drive()
car1.start()

def validate_year(year):
    try:
        year = int(year)

        if year < 1900:
            return None, "Invalid year"
        else:
            return year, "Valid year"
    except ValueError:
        return None, "Year must be a number"

print(validate_year(2025))
print(validate_year(1800))
print(validate_year("hello"))

year_result = validate_year(2026)
print(year_result)
valid_year, status = validate_year(2026)
print(valid_year)
print(status)
valid_year, status = validate_year(2026)
if status == "Valid year":
    car1.update_year(valid_year)
  
