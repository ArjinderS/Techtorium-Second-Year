#Week 2 Tuesday

class Animals():
    def __init__(self) -> None:
        pass

    def make_sound():
        print("Pretend a sound is made")

class Dog(Animals):
    pass
    #Ovveride the make_sound method in the dog class to make a barking sound

class Person():
    def __init__(self, name, age):
        name = "Connor"
        age = "18"

class Skills():
    def __init__(self, programming_skill, communication_skill):
        pass

class Employee(): #inherit from person and skills
    pass

class Vehicle():
    def start_engine():
        print("Engine started")

class Car(Vehicle):
    #some stuff
    def drive():
        print("Car is driving")

class ElectricCar(Car):
    def charge_battery():
        print("Car battery is charging")