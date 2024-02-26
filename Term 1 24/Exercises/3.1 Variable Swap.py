#3.1 Variable Swap
#Not sure on this one

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