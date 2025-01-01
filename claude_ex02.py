# Alternative Binary Search Variations

# 1. Binary Search with Range Finding
def binary_search_range(arr, target):
    """Find first and last position of target in sorted array"""
    def find_bound(is_left):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target or (is_left and arr[mid] == target):
                right = mid
            else:
                left = mid + 1
        return left
    
    left = find_bound(True)
    if left >= len(arr) or arr[left] != target:
        return [-1, -1]
    return [left, find_bound(False) - 1]

# Questions:
# A: The implementation can handle duplicates correctly 
# B: The function returns correct indices for target at array bounds
# C: The use of 'len(arr)' instead of 'len(arr)-1' is a bug
# D: The second binary search is unnecessary as we can scan linearly after finding left bound

# Binary Search Range:
# A: True (handles duplicates through separate bound finding)
# B: True (boundary conditions are properly handled)
# C: False (intentional for this implementation)
# D: False (linear scan would make it O(n) in worst case)

# 2. Modified QuickSort with Three-Way Partition
def quicksort_three_way(arr, low, high):
    """QuickSort with handling for equal elements"""
    if low >= high:
        return
    
    lt = low  # Elements less than pivot
    gt = high  # Elements greater than pivot
    i = low + 1  # Current element
    pivot = arr[low]
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    quicksort_three_way(arr, low, lt - 1)
    quicksort_three_way(arr, gt + 1, high)

# Questions:
# A: The algorithm maintains stability for equal elements 
# B: The implementation handles the case when all elements are equal efficiently 
# C: The pivot selection strategy could be improved for better performance 
# D: The algorithm requires extra space for handling the three-way partition 

# QuickSort Three-Way:
# A: False (quicksort variations are inherently unstable)
# B: True (equal elements are handled in O(n))
# C: True (random pivot would be better)
# D: False (partitioning is done in-place)


# 3. LeetCode-Style Problems

# Problem 1: Chemical Waste Detection
"""
Given an array of sensor readings and a threshold k, find the minimum length subarray
whose sum is greater than k. The readings are from nearby sensors, so the subarray
must be contiguous.

Example:
Input: readings = [1,4,2,3,6,2], k = 8
Output: 2
Explanation: Subarray [6,2] has sum 8 which is > k
"""

def min_subarray_sum_greater(readings, k):
    n = len(readings)
    min_len = float('inf')
    curr_sum = 0
    left = 0
    
    for right in range(n):
        curr_sum += readings[right]
        while curr_sum > k:
            min_len = min(min_len, right - left + 1)
            curr_sum -= readings[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# Questions:
# A: The algorithm handles negative numbers correctly
# B: The time complexity is O(n) where n is the length of readings
# C: The algorithm could be optimized by sorting the array first
# D: The while loop condition should be curr_sum >= k

# Problem 1:
# A: False (problem specifies positive readings)
# B: True (sliding window gives O(n))
# C: False (sorting would break contiguous property)
# D: False (current condition is correct for strictly greater)


# Problem 2: Malfunction Detection
"""
You have an array of sensor readings where some sensors are malfunctioning and reporting
duplicate values. Given a sorted array, find the count of unique values efficiently.

Example:
Input: readings = [1,1,2,2,3,4,4,4,5]
Output: 5
"""

def count_unique_readings(readings):
    if not readings:
        return 0
        
    unique_count = 1
    for i in range(1, len(readings)):
        if readings[i] != readings[i-1]:
            unique_count += 1
    
    return unique_count

# Questions:
# A: The implementation requires the input to be sorted
# B: The space complexity is O(1)
# C: Using a set would be more efficient for this problem
# D: The initialization of unique_count to 1 could cause issues with empty arrays

# Problem 2:
# A: True (relies on sorted property)
# B: True (only uses constant extra space)
# C: False (set would be O(n) space and wouldn't preserve order)
# D: True (should handle empty array case first)


# Problem 3: Heap Verification with Constraints
"""
Implement a function to verify if an array represents a valid min-heap with the additional
constraint that each parent must be at least 50% smaller than its children.

Example:
Input: [1, 3, 2, 7, 8, 4, 5]
Output: False (2 is not 50% smaller than 4)
"""

def is_valid_heap_with_constraint(arr):
    def parent(i): return (i - 1) // 2
    def left(i): return 2 * i + 1
    def right(i): return 2 * i + 2
    
    for i in range(1, len(arr)):
        p = parent(i)
        if arr[p] * 1.5 > arr[i]:
            return False
    return True

# Questions:
# A: The implementation correctly handles the 50% constraint
# B: The function needs to check both children explicitly
# C: The parent calculation could cause integer division issues
# D: The loop should start from index 0 instead of 1

# Correct Answers and Explanations:
"""
Problem 3:
A: False (missing checks for right child)
B: True (need explicit checks for both children)
C: False (integer division is appropriate here)
D: False (starting from 1 is correct for heap property)
"""

# Additional Implementation Challenges:

"""
1. Modify the binary search to find the closest element if exact match not found
2. Implement QuickSort with random pivot selection and handling for small subarrays
3. Create a hybrid sort that switches between algorithms based on input size
4. Design a heap implementation that supports efficient decrease-key operation
"""