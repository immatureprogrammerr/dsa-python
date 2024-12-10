
def merge(left_half, right_half):
    c  = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            c.append(left_half[i])
            i += 1
        else:
            c.append(right_half[j])
            j += 1

    if i < len(left_half):
        for _ in range(i, len(left_half)):
            c.append(left_half[i])
            i += 1

    if j < len(right_half):
        for _ in range(j, len(right_half)):
            c.append(right_half[j])
            j += 1
    return c

def merge_sort(array):

    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


array = [9, 4, 1, 34, 2, 6, 12]
print(merge_sort(array))