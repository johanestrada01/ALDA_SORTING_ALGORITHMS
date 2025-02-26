def radix_sort(arr):  # O(n) = O(d * (n + k))
    digits = len(str(max(arr)))  # O(d) 
    for i in range(digits):  # O(d)
        arr = counting_sort(arr, i)  # O(n + k)
    return arr  # O(1)

def counting_sort(arr, i):  # O(n + k)
    frequencies = [0] * 10  # O(k) = O(10) = O(1)  
    sorted_array = [0] * len(arr)  # O(n)
    for value in arr:  # O(n)
        frequencies[((value // (10 ** i)) % 10)] += 1  # O(1)
    for j in range(1, 10):  # O(k) = O(10) = O(1)
        frequencies[j] += frequencies[j - 1]  # O(1)
    for value in reversed(arr):  # O(n)
        current_value = ((value // (10 ** i)) % 10)  # O(1)
        index = frequencies[current_value] - 1  # O(1)
        sorted_array[index] = value  # O(1)
        frequencies[current_value] -= 1  # O(1)
    return sorted_array  # O(1)
