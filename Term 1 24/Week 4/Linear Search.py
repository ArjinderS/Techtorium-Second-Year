
#Linear Search

def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
 
 
if __name__ == "__main__":
    sorted_values = [12, 24, 30, 42, 55, 63, 75, 82, 91, 99]
    x = 10
    N = len(sorted_values)
 
    result = search(sorted_values, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)