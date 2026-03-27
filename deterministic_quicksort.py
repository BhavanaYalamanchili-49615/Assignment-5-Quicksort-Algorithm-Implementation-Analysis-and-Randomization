# Partition function chose the final element as the pivot and organized values in terms of comparison.
# Quicksort function broke array down into smaller segments and sorted with the help of recursion.

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
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # sorting left part
        quicksort(arr, low, pi - 1)

        # sorting right part
        quicksort(arr, pi + 1, high)


# creating sample list
arr = [10, 7, 8, 9, 1, 5]

# calling sorting function
quicksort(arr, 0, len(arr) - 1)

# printing sorted result
print(arr)