# Partition divided into middle element on which it pivoted and sorted values with partition logic.
# Test function was used to compare the performance of quicksort and randomized quicksort with various types of inputs.

import time
import random

# selecting middle element as pivot and arranging elements
def partition(arr, low, high):
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]

    pivot = arr[high]
    i = low - 1

    # comparing each element with pivot and swapping when needed
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # placing pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# dividing array and sorting using recursion
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # sorting left part
        quicksort(arr, low, pi - 1)

        # sorting right part
        quicksort(arr, pi + 1, high)


# selecting random pivot and swapping with last element
def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # calling partition to arrange elements
    return partition(arr, low, high)


# dividing array and sorting using recursion
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)

        # sorting left part
        randomized_quicksort(arr, low, pi - 1)

        # sorting right part
        randomized_quicksort(arr, pi + 1, high)


# measuring execution time for sorting
def test_sorting(sort_function, arr):
    start = time.time()

    # calling sorting function
    sort_function(arr, 0, len(arr) - 1)

    end = time.time()

    # returning time taken
    return end - start


# defining input sizes
sizes = [1000, 5000, 10000]

# running tests for different sizes
for size in sizes:
    # creating random input
    arr_random = [random.randint(1, 10000) for _ in range(size)]

    # creating sorted input
    arr_sorted = sorted(arr_random)

    # creating reverse sorted input
    arr_reverse = sorted(arr_random, reverse=True)

    print("\nSize:", size)

    # testing deterministic quicksort
    print("Deterministic Random:", test_sorting(quicksort, arr_random.copy()))
    print("Deterministic Sorted:", test_sorting(quicksort, arr_sorted.copy()))
    print("Deterministic Reverse:", test_sorting(quicksort, arr_reverse.copy()))

    # testing randomized quicksort
    print("Randomized Random:", test_sorting(randomized_quicksort, arr_random.copy()))
    print("Randomized Sorted:", test_sorting(randomized_quicksort, arr_sorted.copy()))
    print("Randomized Reverse:", test_sorting(randomized_quicksort, arr_reverse.copy()))