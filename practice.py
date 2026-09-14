with open("student.txt", "r") as file:
    content = file.read()
    print(content)
    file.seek(0)
    content = file.read()
    print(content)

with open("student.txt", "r") as file:
    print(file.tell())
    content = file.read()
    print(file.tell())
    file.seek(0)
    print(file.tell())

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand}, {self.model} is starting")


car1  = Car("Toyota", "Camry", 2024)

print(car1.model)
car1.model = "Corolla"
car1.year = 2025
car1.display_info()



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand}, {self.model} is starting")


car1 = Car("Toyota", "Camry", 2024)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("BMW", "X5", 2025)

car1.display_info()
car2.display_info()
car3.display_info()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def change_year(self, new_year):
        self.year = new_year
    
    def display_info(self):
        print(f"{self.brand}, {self.model}, {self.year}")

car1 = Car("Toyota", "camry", 2024)
car1.change_year(2026)
car1.display_info()

class Car:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def update_car(self, new_model, new_year):
        self.model = new_model
        self.year = new_year

    def display_info(self):
        print(f"{self.brand}, {self.model}, {self.year}")

car1 = Car("Toyota", "Camry", 2024)
car1.update_car("Corolla", 2026)
car1.display_info()


class Vehicle:
    def start(self):
        print("Vehicle is starting")
    
class Car(Vehicle):
    pass

car1 = Car()
car1.start()