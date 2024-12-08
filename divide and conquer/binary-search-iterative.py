import math

def binary_search_iterative(array, key):
    low = 0
    high = len(array) - 1

    while low <= high: 
        mid = math.floor((low + high) / 2)
        if key == array[mid]:
            return mid
        if key > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 0

array = [2, 8, 9, 11, 34, 56, 78, 90]
print(binary_search_iterative(array, 8))