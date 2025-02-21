import sys
def merge_sort(arr):  #O(n) = n log n
    if len(arr) <= 1:  # O(1)
        return arr  
    mid = len(arr) // 2  # O(1)
    left_half = merge_sort(arr[:mid])   # O(n log n)
    right_half = merge_sort(arr[mid:])  # O(n log n)
    return merge(left_half, right_half)  # O(n)

def merge(left, right):
    sorted_array = []  # O(1)
    i = j = 0  # O(1)
    while i < len(left) and j < len(right):  # O(n)
        if left[i] < right[j]:  # O(1)
            sorted_array.append(left[i])  # O(1)
            i += 1  # O(1)
        else:
            sorted_array.append(right[j])  # O(1)
            j += 1  # O(1)
    sorted_array.extend(left[i:])  # O(n)
    sorted_array.extend(right[j:])  # O(n)
    return sorted_array  # O(1)


