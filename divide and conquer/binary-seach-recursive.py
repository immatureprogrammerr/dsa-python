import math

def binary_search_recursive(array, key):
    def helper(low, high):
        if low == high:
            if array[low] == key:
                return low
            else: 
                return 0
        else:
            mid = math.floor((low+high)/2)
            
            if key == array[mid]:
                return mid
            if key < array[mid]:
                return helper(low, mid - 1)
            else:
                return helper(mid + 1, high)
    
    low = 0
    high = len(array) - 1
    return helper(low, high)


array = [2, 8, 9, 11, 34, 56, 78, 90]
print(binary_search_recursive(array, 8))