# 1. Binary Search with Edge Cases
def binary_search(arr, target):
    left = 0
    right = len(arr)  # Subtle bug: should be len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoiding potential overflow
        
        if mid >= len(arr):  # Protection against index out of range
            return -1
            
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Questions for Binary Search:
# A: The implementation is correct for all edge cases
# B: The protection against index out of range is unnecessary since the while condition prevents it
# C: The mid calculation could lead to integer overflow in Python
# D: The initial right value causes the algorithm to miss the last element

# 2. QuickSort with Pivot Selection
def quicksort(arr, low, high):
    def partition(low, high):
        pivot = arr[high]  # Using last element as pivot
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low >= high:
        return
        
    pi = partition(low, high)
    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

# Questions for QuickSort:
# A: The partition function correctly handles duplicate elements
# B: The implementation is stable (maintains relative order of equal elements)
# C: The base case condition should be "if low > high" instead of "if low >= high"
# D: The pivot selection method could lead to O(n²) complexity for already sorted arrays

# 3. Selection Sort with Optimization
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:  # Optimization: only swap if necessary
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Questions for Selection Sort:
# A: The optimization of checking min_idx != i reduces the number of comparisons
# B: The outer loop should run from range(n) instead of range(n-1)
# C: The inner loop should start from i+1 instead of i
# D: The algorithm maintains stability for equal elements

# 4. Checking Min-Heap Property
class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def is_min_heap(self):
        n = len(self.heap)
        for i in range(1, n):
            if self.heap[i] < self.heap[self.parent(i)]:
                return False
        return True

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._bubble_up(parent)

# Questions for Min-Heap:
# A: The is_min_heap method correctly validates all heap properties
# B: The range in is_min_heap should start from 0 instead of 1
# C: The parent method could return a negative index for i=0
# D: The bubble_up method maintains heap property efficiently

# Correct Answers:
"""
Binary Search:
- A: False (right should be len(arr)-1)
- B: False (protection is needed due to the bug in right initialization)
- C: False (Python integers have unlimited precision)
- D: True

QuickSort:
- A: True
- B: False (quicksort is inherently unstable)
- C: False (current condition is correct)
- D: True

Selection Sort:
- A: False (doesn't reduce comparisons, only swaps)
- B: False (n-1 is correct as last element will be in place)
- C: True
- D: False

Min-Heap:
- A: False (doesn't check right child property)
- B: False (starting from 1 is correct)
- C: False (parent method works correctly for all valid indices)
- D: True
"""