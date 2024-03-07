
#Stellar Events 


operation_selection = ["A", "S", "D", "U", "E"] #Variable to select an operation
vendors_list = [] #Defining an empty vendors list

#While loop acts as a main menu to return to following an operation 
while True:
    operation = input("\nWelcome to Stellar Events! To choose an operation, type:\nA to add a vendor's contact details,\nS to search current vendors,\nD to delete from the list of vendors,\nU to update from list of current vendors, or\nE to add extra details to current vendors:")

    if operation.lower() == "a":
        if len(vendors_list) >= 10:
            print("You have reached the limit for vendors contact details.")
        else:
            vendorname = input("\nEnter name: ")
            vendorphone = input("Enter phone number: ")
            vendoremail = input("Enter email address: ")
            vendors_list.append({"name": vendorname, "phone": vendorphone, "email": vendoremail})
            print("\nThe vendor {} has been added.\nTheir details below:\nPhone Number: {}\nEmail Address: {}".format(vendorname, vendorphone, vendoremail))
    elif operation.lower() == "s":
        search_query = input("\nEnter search query: ").lower()
        found_vendors = []
        for vendor in vendors_list:
            if search_query in vendorname.lower() or search_query in vendorphone.lower() or search_query in vendoremail.lower():
                found_vendors.append(vendor)
        if found_vendors:
            print("\nSearch results:")
            for index, vendor in enumerate(found_vendors, 1):
                print("{}: {}\nPh: {}\nEmail: {}\n".format(index, vendor["name"], vendor["phone"], vendor["email"]))
        else:
            print("Invalid search")
    elif operation.lower() == "d":
        delete_index = int(input("Enter the index of the vendor you want to delete (1 - 10): "))
        if delete_index >= 1 and delete_index <= len(vendors_list):
            deleted_vendor = vendors_list.pop(delete_index - 1)
            print("Vendor {} deleted.".format(deleted_vendor["name"]))
        else:
            print("Invalid index")
    elif operation.lower() == "u":
        update_index = int(input("Enter the index of a vendor you want to update: "))
        if update_index >= 1 and update_index <= len(vendors_list):
            vendor = vendors_list[update_index - 1]
            vendor["name"] = input("Enter updated name: ")
            vendor["phone"] = input("Enter updated phone number: ")
            vendor["email"] = input("Enter updated email address: ")
            print("Your vendors details have been updated")
        else:
            print("Invalid index.")
    elif operation.lower() == "e":
        update_index = int(input("Enter the index of a vendor to add extra details to: "))
        if update_index >= 1 and update_index <= len(vendors_list):
            vendor = vendors_list[update_index - 1]
            extra_details = input("Enter extra details: ")
            vendor["extra_details"] = extra_details
            print("Details have been added to vendor {}.".format(vendor["name"]))
        else:
            print("Invalid index.")
    else:
        print("Input doesn't match given operation")

    next_action = input("\nPress any key to run a new operation or 'Q' to quit: ")
    if next_action.upper() == "Q":
        break