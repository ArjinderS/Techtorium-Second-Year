
#Stellar Events 

#

operation_selection = ["A", "S", "D", "V"] #Variable to select an operation (Add, Search/View, Delete) Need to add View All
vendors_list = [] #Defining an empty vendors list

#While loop acts as a main menu to return to following an operation 
while True:
    operation = input("\nWelcome to Stellar Events! To choose an operation, type:\nA to add a vendor's contact details,\nS to search or view current vendors,\nD to delete from the list of vendors,\nV to view the list of added vendors,\nSelect your operation here: ")
    
    #Method to add vendor contact details
    if operation.lower() == "a": #operation.lower allows users input to not be case sensitive
        if len(vendors_list) >= 10: #If maximum amount of vendors reached
            print("You have reached the limit for vendors contact details.")
        else:
            vendorname = input("\nEnter name: ")
            vendorphone = input("Enter phone number: ")
            vendoremail = input("Enter email address: ")
            vendors_list.append({"name": vendorname, "phone": vendorphone, "email": vendoremail}) #Add vendor's inputs to list
            print("\nThank you for attending Stellar Events. The vendor {} has been added.\nTheir details below:\nPhone Number: {}\nEmail Address: {}".format(vendorname, vendorphone, vendoremail))
    
    #Method to search and then view vendor contact details    
    elif operation.lower() == "s":
        search_query = input("\nEnter search query: ").lower() #input().lower() allows for a search query to not be case sensitive
        found_vendors = [] #Defining an empty list to display found vendors
        for vendor in vendors_list:
            if search_query in vendorname.lower() or search_query in vendorphone.lower() or search_query in vendoremail.lower():
                found_vendors.append(vendor)
        if found_vendors:
            print("\nSearch results:")
            for index, vendor in enumerate(found_vendors, 1): #Returns vendors found from initial list
                print("{}: {}\nPh: {}\nEmail: {}\n".format(index, vendor["name"], vendor["phone"], vendor["email"])) #Displays vendor information (View SR1.2)
        else:
            print("Invalid search") #No results returned
    
    #Method to delete contact vendor details
    elif operation.lower() == "d":
        delete_index = int(input("Enter the index of the vendor you want to delete (1 - 10): ")) #Integer input to delete a certain vendor
        if delete_index >= 1 and delete_index <= len(vendors_list): #If integer given is equal to or larger than 1, and is found in vendor list
            deleted_vendor = vendors_list.pop(delete_index - 1) #Remove selected vendor
            print("Vendor {} deleted. Thank you for attending Stellar Events".format(deleted_vendor["name"]))
        else:
            print("Invalid index") #No vendor found
    
    #Method to view all currently added vendors
    elif operation.lower() == "v": #if V is selected during main menu process
        for vendor in vendors_list:
            if len(vendors_list) <= 10: #If vendor list is less than or equal to 10 (maximum number of vendors)
                for index, vendor in enumerate(vendors_list, 1): #Returns vendors found from initial list
                    print("{}: {}\nPh: {}\nEmail: {}\n".format(index, vendor["name"], vendor["phone"], vendor["email"]))
            elif len(vendors_list) <= 0: #Else if vendor list contains nothing 
                print("No vendors currently in list.")
  
    #If incorrect input is given during main menu process (Add, Search, Delete or View not selected)
    else:
        print("Input doesn't match given operation")

    next_action = input("\nPress any key to run a new operation or 'Q' to quit: ")
    if next_action.upper() == "Q":
        print("Thank you for attending Stellar Events")
        break