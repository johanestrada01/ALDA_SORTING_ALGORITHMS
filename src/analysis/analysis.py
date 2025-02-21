from algorithms.bubble_sort import bubble_sort
from algorithms.counting_sort import counting_sort
from algorithms.merge_sort import merge_sort
from algorithms.radix_sort import radix_sort
import random
import time
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

sizes = [10, 100, 1000, 5000, 10000]

test_lists = []

for size in sizes:
    current_list = []
    for j in range(size):
        current_list.append(random.randint(0, 100000000))
    test_lists.append(current_list)

times_bubble = []
for case in range(len(test_lists)):
    test = test_lists[case][:]
    initial_timee = time.time()
    bubble_sort(test)
    times_bubble.append(time.time() - initial_timee)


times_merge = []
for case in range(len(test_lists)):
    test = test_lists[case][:]
    initial_timee = time.time()
    merge_sort(test)
    times_merge.append(time.time() - initial_timee) 


times_radix = []
for case in range(len(test_lists)):
    test = test_lists[case][:]
    initial_timee = time.time()
    radix_sort(test)  
    times_radix.append(time.time() - initial_timee) 

times_counting = []
for case in range(len(test_lists)):
    test = test_lists[case][:]
    initial_timee = time.time() 
    counting_sort(test)
    times_counting.append(time.time() - initial_timee)  


plt.plot(sizes, times_bubble, marker="o", label="Bubble Sort")
plt.plot(sizes, times_merge, marker="s", label="Merge Sort")
plt.plot(sizes, times_radix, marker="o", color="r", label="Radix Sort")
plt.plot(sizes, times_counting, marker="s", color="b", label="Counting Sort")


plt.xlabel("Size of array")
plt.ylabel("Time (seconds)")
plt.title("Sorting algorithms")
plt.legend()
plt.grid()
plt.show()


##Preguntar tamaños de memoria, casos (grafica por cada caso), graficas