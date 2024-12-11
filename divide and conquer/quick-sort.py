def quick_sort(array):

    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    less_than_pivot = [x for x in array[:-1] if x <= pivot]
    greater_than_pivot = [x for x in array[:-1] if x > pivot]

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

array = [9, 7, 6, 3, 1, 12]
print(quick_sort(array))