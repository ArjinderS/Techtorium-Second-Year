#5.2 Nested If Statements

# Default function to run if else condition  
def NumberCheck(a):   
    # Checking if the number is positive  
    if a > 0:   
        print("The number you gave is positive")   
    # Checking if the number is negative   
    elif a < 0:   
        print("The number you gave is negative")   
    # Else the number is zero  
    else:   
        print("The number you gave is Zero")  
# Taking number from user  
a = float(input("Enter a number as input value: "))  
# Printing result  
NumberCheck(a) 