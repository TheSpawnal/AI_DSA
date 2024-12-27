

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found the element
        if arr[mid] == x:
            return mid
        # Element is in the right half
        elif arr[mid] < x:
            left = mid + 1
        # Element is in the left half
        else:
            right = mid - 1
    
    # Element not found
    return -1