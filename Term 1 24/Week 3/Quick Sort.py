
#Quick Sort

def partition(array, low, high):
	pivot = array[high]
	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:
			
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

data = [67, 12, 89, 43, 56, 34, 78, 23, 
		91, 45, 18, 76, 39, 52, 87, 65, 
		29, 83, 16, 72, 47, 54, 31, 95, 
		68, 21, 84, 59, 13, 75]
print("Given Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('\nSorted Array in Ascending Order:')
print(data)
