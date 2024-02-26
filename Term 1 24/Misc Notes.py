''''
#Misc Notes

#Inheritance
inheritance allows you to define a subclass that inherits 
all the attributes and functions of its parent class which 
is called through a parameter. you're able to override for 
example the init function by putting your one under the 
subclass, or calling the parent class so that it doesn't override

class Parent:
	def __init__(variable?):
	#add objects

class Child(Parent):
pass

Runtime vs compile time
Ststic and dynamic languages are different as they compile their 
variables at different times.

Data structures
[ Lists ] - heterogenious list (they all are)
list index always starts with 0
Lists can hold different types of information such as strings, 
integers, dictionaries, stacks, tuples and other data types
mutable means you are able to come back to a list and edit it
after it has been created
printing a certain answer in a list
 0,  1,  2,  3,  4 Normal list
-5, -4, -3, -2, -1 calling the item print(list(-1)) (to print 4)
thislist = ["apple", "banana", "cherry"]
print(thislist)

( Tuple )
imutable - not modifiable or able to come back to edit
ordered and unchangeable
this means that once the tuple is created you are unable
to come back to it and edit it 
thistuple = ("apple", "banana", "cherry")
print(thistuple)

{ Dictionary }
Set, Stack (Last In First Out), Queue (First in First Out FIFO)

castable
longlist
tree
sets

Week 3 Monday Tuesday (19/20th Feb)
Bubble and Insertion Sorting, Selection, Merge, and Quick Sort

Example Array
[67, 12, 89, 43, 56, 34, 78, 23,
 91, 45, 18, 76, 39, 52, 87, 65,
 29, 83, 16, 72, 47, 54, 31, 95,
 68, 21, 84, 59, 13, 75]

 Bubble switches the first two elements, then then next one over
and over until the whole list is sorted in numerical order
for example 67 and 12 would be switched, then 89 and 43
each time it passes through the entire list that's one iteration
the maximum number of iterations is n-1 (amount of no in list - 1)

Insertion is similar, but it continues to sort a certain number
until it is in it's correct position, until all of them are in 
the right spot. for example 67 and 12 would be switched, then 89 
and 43, however it would keep switching 89 until it's at it's 
respective ascending order, and continues from where it left off,
in this case around 43

Selection
Merge is when your array is split in half, and each half is split
over and over until there are only subarrays of two integers each
in which they are switched and sorted if required, so that when 
they are returned to the main array, (when the subarrays are re-
attached to each other) they should be sorted in ascending order
Quick sort

I've installed a virtual environment venv, by going to the command
palette or typing >Python: Create Environment in vscode, and created
one in my Week 3 folder, however i'm struggling to install pandas 
which i'm not sure why as i have pip installed but the pip install
pandas command isn't working in cmd, so i tried installing anaconda
to import panda into my virtual environment but that didn't seem to
work (i just don't understand how to use anaconda) So after work 
tonight i will try get a few hours in studying and see if i can catch
up on the programs i missed for bubble/insertion, and then go further 
in depth with selection, merging and quick sorts

A common convention is to collect the libraries you need in 
requirements.txt so that you can create a new virtual environment, 
activate it, and pip install -r requirements.txt whenever you need to.

'''