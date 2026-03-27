# Randomized partition function chose pivot on the basis of random index and reorganized elements.
# Randomized quicksort operation minimized the possibility of worst case by selecting randomly.

import random

# selecting random pivot and swapping with last element
def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # calling partition to arrange elements
    return partition(arr, low, high)


# selecting last element as pivot and arranging elements
def partition(arr, low, high):
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
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)

        # sorting left part
        randomized_quicksort(arr, low, pi - 1)

        # sorting right part
        randomized_quicksort(arr, pi + 1, high)


# creating sample list
arr = [10, 7, 8, 9, 1, 5]

# calling sorting function
randomized_quicksort(arr, 0, len(arr) - 1)

# printing sorted result
print(arr)