def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def remove_duplicates(arr):
    """Remove duplicate elements from a list while preserving order"""
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

