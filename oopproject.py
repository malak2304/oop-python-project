from abc import ABC, abstractmethod


class Vehicle(ABC):  # abstract class
    def _init_(self, vehicle_name, vehicle_color, vehicle_year):
        self.vehicle_name = vehicle_name
        self.vehicle_color = vehicle_color
        self.vehicle_year = vehicle_year

    def get_Info(self):
        print(f"\n{self.vehicle_name} Is {self.vehicle_color} And Was Produced In {self.vehicle_year}")  # abstraction

    @abstractmethod
    def number_of_passengers(self):
        pass


class Motorcycle(Vehicle):
    def _init_(self, vehicle_name, vehicle_color, vehicle_year, motocycle_price):
        Vehicle._init_(self, vehicle_name, vehicle_color, vehicle_year)  # Encapsulation And Inheritance
        self.__motocycle_price = motocycle_price  # Privet Attribute

    # Setter And Getter
    def set_price(self, new_price):
        self.__motocycle_price = new_price

    def get_price(self):
        print(f"{self.vehicle_name} Price Is {self.__motocycle_price}$")

    def number_of_passengers(self):
        print("Number Of Passenger = 2 \n")


class Car(Vehicle):
    def _init_(self, vehicle_name, vehicle_color, vehicle_year, vehicle_max_speed):
        Vehicle._init_(self, vehicle_name, vehicle_color, vehicle_year)
        self.__vehicle_max_speed = vehicle_max_speed  # Privet Attribut

    # Setter And Getter
    def set_Speed(self, new_max_speed):
        self.__vehicle_max_speed = new_max_speed  # Encapsulation And Inheritance

    def get_Speed(self):
        print(f"{self.vehicle_name} Max Speed Is {self.__vehicle_max_speed} km/h")

    def number_of_passengers(self):
        print("Number Of Passenger = 4 \n")


class Plane(Vehicle):
    def _init_(self, vehicle_name, vehicle_color, vehicle_year):
        Vehicle._init_(self, vehicle_name, vehicle_color, vehicle_year)  # Inheritance And Polymorphism
        self.__vehicle_color = vehicle_color

    # Setter And Getter
    def set_color(self, new_color):
        self.__vehicle_color = new_color

    def get_color(self):
        print(f"{self.vehicle_name} Color Is {self.__vehicle_color}")

    def number_of_passengers(self):
        print("Number Of Passenger = 140 - 250 \n")

    # Polymorphism And Override
    def get_Info(self):
        print(
            f"\n{self.vehicle_name} Is {self.vehicle_color} And Was Produced In {self.vehicle_year} And The Plane Is flying In The Sky")


class Ship(Vehicle):
    def _init_(self, vehicle_name, vehicle_color, vehicle_year, vehicle_load):
        Vehicle._init_(self, vehicle_name, vehicle_color, vehicle_year)  # Polymorphism And Inheritance
        self.__vehicle_load = vehicle_load

    # Setter And Getter
    def set_load(self, new_load):
        self.__vehicle_load = new_load

    def get_load(self):
        print(f"{self.vehicle_name} Load Is {self.__vehicle_load}Kg")

    def number_of_passengers(self):
        print("Number Of Passenger = 80 - 100\n")

    # Polymorphism And Override
    def get_Info(self):
        print(
            f"\n{self.vehicle_name} Is {self.vehicle_color} And Was Produced In {self.vehicle_year} And I Sail In Sea And Oceans")


# Objects
v1 = Motorcycle("Honda", "Red", "2004", "10000")
v2 = Car("Bmw", "Black", "2005", "250")
v3 = Plane("Airbus A320 Series", "White", "1984")
v4 = Ship("AquaNova", "Blue", "1950", "430000")

# Motocycle Class
v1.get_Info()
v1.number_of_passengers()
# Setter And Getter
v1.get_price()
v1.set_price("15000")
v1.get_price()

print("#" * 50, "\n")

# Car Class
v2.get_Info()
v2.number_of_passengers()
# Setter And Getter
v2.get_Speed()
v2.set_Speed("280")
v2.get_Speed()

print("#" * 50, "\n")

# Plane Class
v3.get_Info()
v3.number_of_passengers()
# Setter And Getter
v3.get_color()
v3.set_color("Green")
v3.get_color()

print("#" * 50, "\n")

# Ship Class
v4.get_Info()
v4.number_of_passengers()
# Setter And Getter
v4.get_load()
v4.set_load("500000")
v4.get_load()

print("#" * 50, "\n")