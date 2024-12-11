# Non-in-place implementation of quick sort
def quick_sort_non_inplace(array):

    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    less_than_pivot = [x for x in array[:-1] if x <= pivot]
    greater_than_pivot = [x for x in array[:-1] if x > pivot]

    return quick_sort_non_inplace(less_than_pivot) + [pivot] + quick_sort_non_inplace(greater_than_pivot)

array = [9, 7, 6, 3, 1, 12]
print(quick_sort_non_inplace(array))