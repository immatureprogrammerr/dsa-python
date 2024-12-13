# Approach 1
def reverse_array(array, start, end):
    while(start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1
    return array

def left_rotate(array, k):
    # reverse all the numbers
    reverse_array(array, 0, len(array) - 1)
    # reverse the first k numbers
    reverse_array(array, 0, len(array) - k - 1)
    # reverse the last k numbers
    reverse_array(array, len(array) - k, len(array) - 1)
    return array

def right_rotate(array, k):
    # reverse all the numbers
    reverse_array(array, 0, len(array) - 1)
    # reverse the first k numbers
    reverse_array(array, k, len(array)- 1)
    return array

array = [2, 3, 4, 5, 6, 7]
print(array)
result1 = left_rotate(array, 1)
print(result1)
result2 = right_rotate(array, 1)
print(result2)
