def bubble_sort(arr): #O(n) = n²
    n = len(arr)  # O(1)
    for i in range(n):  # O(n)
        swapped = False  # O(1)
        for j in range(n - i - 1):  # O(n - i) → in the worst case O(n)
            if arr[j] > arr[j + 1]:  # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)
                swapped = True  # O(1)
        if not swapped:  # O(1)
            break  # O(1) in the best case
    return arr  # O(1)
