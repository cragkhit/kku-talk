# Bubble Sort Implementation in Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Method to remove duplicates from a sorted array
def remove_duplicates(arr):
    if not arr:
        return arr
    unique_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])
    return unique_arr