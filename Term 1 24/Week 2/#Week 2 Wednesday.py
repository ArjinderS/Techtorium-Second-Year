#Week 2 Wednesday

#List Exercises
print("Exercise 1: Original shopping list:")
shopping_list = []
shopping_list.extend(["apple", "banana", "orange"])
print("Updated shopping list:", shopping_list)

print("\nExercise 2:")
shopping_list.append("grapes")
if "banana" in shopping_list:
    shopping_list.remove("banana")
print("Final shopping list:", shopping_list)

#Tuple Exercises
#coordinates = ("Latitude Value: ", + y, + "Longitude Value: ", + x)
#y = 6
#x = 4
coordinates = (50, -100)
def display_coordinates(coords):
    print("Latitude:", coords[0])
    print("Longitude:", coords[1])

def update_latitude(coords, new_latitude):
    updated_coords = (new_latitude, coords[1])
    return updated_coords
print("Initial coordinates:")
display_coordinates(coordinates)
print()
new_latitude = int(input("Enter the new latitude: "))
coordinates = update_latitude(coordinates, new_latitude)
print("\nUpdated coordinates:")
display_coordinates(coordinates)

fruits = ("apple", "banana", "orange")
print("\nThe second fruit is:", fruits[1])
if "banana" in fruits:
    print("Yea here's your banana now get lost monkey")
else:
    print("Get lost there's no bananas here monkey")

#Dictionary Exercises


#Set Exercises


#Stack Exercises


#Queue Exercises