def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]
        
    array[low], array[j] = array[j], array[low]
    return j

def quick_sort_inplace(array, low, high):
    
    if low < high:
        j = partition(array, low, high)
        quick_sort_inplace(array, low, j - 1)
        quick_sort_inplace(array, j + 1, high)
        
array = [9, 7, 6, 3, 1, 12]
quick_sort_inplace(array, 0, len(array) - 1)
print(array)