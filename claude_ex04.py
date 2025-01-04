# Binary Search Implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Binary Search Desk Check
# Consider the following array: [2, 4, 6, 8, 10, 12, 14] and target = 8

# Which statements are TRUE:
# A) After the first iteration, mid = 3 and the algorithm continues with right = mid - 1
# B) After the first iteration, mid = 3 and the target is found immediately
# C) The algorithm will take exactly 3 iterations to find any number in this array
# D) If we search for 7, the algorithm will return the index of 8

# A) FALSE - After first iteration, mid = 3 and arr[mid] = 8, which equals the target, so the algorithm doesn't continue
# B) TRUE - In the first iteration:
# left = 0, right = 6
# mid = (0 + 6) // 2 = 3
# arr[3] = 8, which equals target
# Algorithm returns 3 immediately

# C) FALSE - The number of iterations depends on where the target is. Some numbers (like 8) are found in 1 iteration
# D) FALSE - The algorithm will return -1 for 7 since it's not in the array


# Quick Sort Implementation
def quicksort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Consider the array: [7, 2, 1, 6, 8, 5, 3] with the last element as pivot

# Which statements are TRUE:
# A) After the first partition, the array will be [2, 1, 3, 5, 8, 6, 7]
# B) The pivot (3) will always be in its final sorted position after partition
# C) The first partition will result in two subarrays of equal size
# D) After the first complete partition, all elements to the left of the pivot will be smaller than the pivot

# A) TRUE - Let's trace first partition with pivot = 3:
# Elements <= 3: [2, 1, 3]
# Elements > 3: [7, 6, 8, 5]
# After arranging: [2, 1, 3, 5, 8, 6, 7]
# B) TRUE - The partition operation ensures the pivot ends up in its final sorted position
# C) FALSE - Partition may create unequal subarrays depending on the pivot value
# D) TRUE - The partition operation ensures all elements left of pivot are smaller than it



# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Consider the array: [5, 2, 8, 1, 9]
# Which statements are TRUE:
# A) The first split creates [5, 2] and [8, 1, 9]
# B) When merging [2, 5] and [1, 8, 9], the first comparison puts 1 at the start
# C) The algorithm will perform exactly 4 merge operations for this array
# D) The sorting process requires exactly 3 levels of recursion

# A) FALSE - First split creates [5, 2] and [8, 1, 9] equally:
# mid = 5/2 = 2
# left = [5, 2]
# right = [8, 1, 9]
# B) TRUE - When merging [2, 5] with [1, 8, 9], 1 is smallest so it goes first
# C) TRUE - Need to merge:
# [5] and [2]
# [8] and [1]
# [1] and [9]
# Final arrays
# D) FALSE - Requires 2 levels: split to [5,2] and [8,1,9], then [5], [2] and [8], [1], [9]



# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Selection Sort Desk Check
# Consider the array: [64, 25, 12, 22, 11]

# Which statements are TRUE:
# A) After the first pass, the array will be [11, 25, 12, 22, 64]
# B) During the second iteration, the minimum value found will be 12
# C) The algorithm will always perform exactly n-1 swaps
# D) After third iteration the array will be [11, 12, 22, 25, 64]

# A) FALSE - After first pass:
# min = 11 found at index 4
# Swap with first element
# Result: [11, 25, 12, 22, 64]
# B) TRUE - In second pass:
# Search range [25, 12, 22, 64]
# min = 12 found
# C) FALSE - Number of swaps depends on initial array order
# D) TRUE - After third iteration:
# First pass: [11, 25, 12, 22, 64]
# Second pass: [11, 12, 25, 22, 64]
# Third pass: [11, 12, 22, 25, 64]





# Check Heap Property Implementation
def is_min_heap(arr):
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

# Consider the array: [4, 10, 3, 5, 1]
# Which statements are TRUE:
# A) This represents a valid min-heap
# B) For index 1, both children violate the heap property
# C) Only the right subtree violates the heap property
# D) The first violation occurs at index 0 with its left child


# A) FALSE - Multiple violations of min-heap property
# B) TRUE 
# Left child (index 3): value 5 (10 > 5, violates min-heap)
# Right child (index 4): value 1 (10 > 1, violates min-heap)

# C) FALSE -
# The left side has violations (10 > 5 and 10 > 1)
# The root itself violates the property with its right child (4 > 3)

# D) FALSE - 


