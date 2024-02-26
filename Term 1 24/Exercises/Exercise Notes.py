#Notes

''''
#Inputs
print('msg:')
x = input()
print('msg' + x)

num1 = int(input("msg"))
num2 = int(input("msg"))
print("msg" + str(num1+num2))

givename = input("msg")
print("msg {} msg".format(givename))

print("""
First line text
Second line text
""")

def personal_details():
    name, age = "Connor", 18
    address = "Auckland, New Zealand"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()

for x in range(5):
    print("msg")
else:
    print("\ndone")


#Variables
    
def swapList(sl,pos1,pos2):
    n = len(sl)     
    # Swapping 
    temp = sl[pos1]
    sl[pos1] = sl[pos2]
    sl[pos2] = temp
    return sl      
l= [1, 2, 3, 4, 5, 6]
pos1= 2
pos2= 5
print(l)
print("Swapped list: ",swapList(l,pos1-1,pos2-1))

Not sure ab this one
str1 = 'hello'
str2 = 'Connor'
result = str1 + ' ' + str2
print(result)

MyAge = 18
print("hello, my name is Connor, and I am ", MyAge, " years old.")
#With function
name = input("Enter name: ")
age = input("Enter age: ")
print("hello, my name is " + name + ", and I am " + age + " years old.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#Add equation
print("The sum of", num1, "and", num2, "is", num1 +-*/ num2)

num1 = float(input("Enter a number representing A: "))
num2 = float(input("Enter a number representing B: "))
if num1 == num2: 
    print("A is equal to B") 
elif num1 < num2: 
    print("A is less than B") 
else: 
    print("A is greater than B") 

age = int(input("Enter age to determine voting eligibility: "))
if age >= 18:
    print("msg")
else:
    print("msg")

#Default function to run if else condition  
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

for num in range(1, 11):
   print(num)
#Different listing style
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(list(range(1, 11)))

#To be continued


'''