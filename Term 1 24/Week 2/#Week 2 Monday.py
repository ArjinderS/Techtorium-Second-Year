#Week 2 Monday

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("\nYour {} {} {} is starting".format(self.year, self.make, self.model))

#del = input()

note1 = ("You gonna drive 2 cars at once??")
note2 = ("Now this is ridiculous")
note3 = ("Who has money for 4 cars")

my_car = Car("Nissan", "Silvia S14 (Kouki)", 1998)
print("Your Nissan's specs:")
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)
my_car.start_engine()

car2 = Car("Mazda", "RX-7 FD", 2002)
car3 = Car("Ford", "Courier", 1998)
car4 = Car("Mitsubishi", "Evo VII", 2001)

print("\n\nYour Mazda's specs:")
print("Make:", car2.make)
print("Model:", car2.model)
print("Year:", car2.year)
car2.start_engine()
print(note1)

print("\n\nYour Ford's specs:")
print("Make:", car3.make)
print("Model:", car3.model)
print("Year:", car3.year)
car3.start_engine()
print(note2)

print("\n\nYour Mitsubishi's specs:")
print("Make:", car4.make)
print("Model:", car4.model)
print("Year:", car4.year)
car4.start_engine()
print(note3)
