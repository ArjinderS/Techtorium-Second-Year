'''
//Deleted Notes
'''

import time

def selectionSort(array, size):
    start_time = time.time()
    
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

arr = [67, 12, 89, 43, 56, 34, 78, 23,
       91, 45, 18, 76, 39, 52, 87, 65,
       29, 83, 16, 72, 47, 54, 31, 95, 
       68, 21, 84, 59, 13, 75]
size = len(arr)
time_taken = selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
print("Algorithm sorted in: {:.6f} seconds".format(time_taken))
