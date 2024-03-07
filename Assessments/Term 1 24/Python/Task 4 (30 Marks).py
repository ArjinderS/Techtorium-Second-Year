
#Tuple Data Structures
def count_inventory(inventory):
    inventory_counts = {}

    for item in inventory: #For loops through the inventory list
        if item in inventory_counts: #If item is already in inventory increment its count
            inventory_counts[item] += 1
        else:
            inventory_counts[item] = 1 #If the item is not in the dictionary, add it with count 1

    total_count = sum(inventory_counts.values()) #read how many items in inventory
    
    return total_count #return how many items in inventory

inventory = ["smartphone", "laptop", "tablet", "smartphone case", "laptop charger", "tablet cover"]
total_items = count_inventory(inventory)
print("\nTotal types of stock in inventory:", total_items)

#SR4.2
supplies = ["pens", "highlighters", "paper", "sticky notes", "staplers"] #list of supplies
print("\n\nThe third office supply is:", supplies[2]) #prints the item with an index of 2 (third item as it starts from 0)
if "sticky notes" in supplies: #If the string sticcky notes is in supplies list, print this, if not print that
    print("\nThere's also sticky notes in here\n")
else:
    print("\nWe're out of sticky notes\n")


my_tuple = (1, 2, 3, 4)
my_tuple.append(5, 6, 7)
print(my_tuple)