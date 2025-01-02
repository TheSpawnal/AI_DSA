# Exercise 1: Tricky Min-Heap Property Checking
# This implementation aims to check if an array represents a min-heap
# with some additional properties
def is_advanced_min_heap(arr, allow_duplicates=False):
    if not arr:
        return True
        
    def has_valid_structure(i):
        size = len(arr)
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check heap property
        is_valid = True
        if left < size:
            if arr[i] > arr[left] or (not allow_duplicates and arr[i] == arr[left]):
                is_valid = False
            else:
                is_valid = is_valid and has_valid_structure(left)
        
        if right < size:
            if arr[i] > arr[right] or (not allow_duplicates and arr[i] == arr[right]):
                is_valid = False
            else:
                is_valid = is_valid and has_valid_structure(right)
                
        return is_valid
        
    return has_valid_structure(0)

# Which statements are true about this implementation?
# A. The function will return True for array [4, 5, 6, 7] when allow_duplicates=True
# B. The recursive has_valid_structure call could lead to stack overflow for very large heaps
# C. The implementation prevents duplicate values in parent-child relationships when 
#    allow_duplicates=False
# D. For array [2, 2, 3] the function returns True when allow_duplicates=True and 
#    False when allow_duplicates=False
"""
A. False - The array [4, 5, 6, 7] is NOT a valid min-heap because:
For a min-heap, parent nodes must be smaller than their children
At index 0, 4 should have children at indexes 1 (5) and 2 (6)
The relationships satisfy min-heap property, but the structure is incomplete
A complete binary tree would require level filling from left to right

B. True - The recursive implementation can lead to stack overflow because:

Each recursive call consumes stack space
For a heap of size n, the recursion depth could be O(log n)
While unlikely in practice for reasonable heap sizes, very large heaps could exceed stack limits
No tail recursion optimization is possible due to the dual recursive calls

C. True - The implementation prevents duplicates in parent-child relationships when allow_duplicates=False:

The condition (not allow_duplicates and arr[i] == arr[left]) explicitly checks for equality
Returns false if a parent and child have equal values when duplicates aren't allowed
This is stricter than a standard min-heap which typically allows duplicates

D. True - For array [2, 2, 3]:

With allow_duplicates=True: Valid because 2≤2 and both 2≤3
With allow_duplicates=False: Invalid because parent-child nodes have equal values (2=2)
"""





# Exercise 2: Advanced Binary Search
# This implementation includes handling of duplicates and custom comparison

def tricky_binary_search(arr, target, find_first=True, custom_compare=None):
    if not arr:
        return -1
        
    def compare(a, b):
        if custom_compare:
            return custom_compare(a, b)
        return (a > b) - (a < b)
    
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        comparison = compare(arr[mid], target)
        
        if comparison == 0:
            result = mid
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
        elif comparison < 0:
            left = mid + 1
        else:
            right = mid - 1
            
    return result

# Which statements are true about this implementation?

# A. For array [1, 2, 2, 2, 3] searching for 2 with find_first=True returns index 1
# B. The implementation will fail if the custom_compare function returns values other 
#    than -1, 0, or 1
# C. Using left + (right - left) // 2 instead of (left + right) // 2 prevents integer 
#    overflow for very large arrays
# D. The function will return the last occurrence of target when find_first=False
"""
A. True - For array [1, 2, 2, 2, 3] searching for 2:

With find_first=True, it returns index 1 (first occurrence)
The algorithm continues searching left side after finding a match when find_first=True
This ensures finding the leftmost occurrence of duplicate values

B. False - The implementation will work with any comparison values:

The comparison result is only used in conditions (< 0, == 0, > 0)
Any positive value is treated as greater
Any negative value is treated as less
Only zero is treated as equal

C. True - Using left + (right - left) // 2:

Prevents integer overflow that could occur with (left + right) // 2
When left and right are large numbers, their sum could exceed maximum integer value
The alternative formula mathematically equivalent but safer
This is particularly important for large arrays or when using smaller integer types

D. True - When find_first=False:

The algorithm continues searching the right side after finding a match
This ensures finding the rightmost occurrence of duplicate values
Returns the highest index where target is found
"""












# Exercise 3: Quick Sort with Three-Way Partitioning
def three_way_quicksort(arr):
    def partition(low, high):
        if high <= low:
            return
            
        lt = low
        gt = high
        i = low + 1
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
                
        partition(low, lt - 1)
        partition(gt + 1, high)
    
    if not arr:
        return arr
    partition(0, len(arr) - 1)
    return arr

# Which statements are true?
# A. The implementation will correctly handle arrays with all equal elements in O(n) time
# B. The partitioning scheme creates three sections: elements less than pivot, 
#    equal to pivot, and greater than pivot
# C. The worst case time complexity is still O(n^2) when the array is already sorted
# D. The implementation modifies the original array in-place
"""
A. True - Handles equal elements in O(n) time because:

Equal elements are grouped together without additional recursion
Only one pass through the array is needed for all equal elements
No unnecessary swaps or comparisons for equal elements
The partitioning scheme naturally handles duplicates efficiently

B. True - The three sections are:

Elements less than pivot (low to lt-1)
Elements equal to pivot (lt to gt)
Elements greater than pivot (gt+1 to high)
This is more efficient than standard two-way partitioning for arrays with many duplicates

C. True - Worst case is still O(n²):

If the pivot is consistently the smallest or largest element
This can happen with an already sorted array
Could be mitigated with better pivot selection strategies
However, the three-way partition helps with equal elements

D. True - In-place modification:

No auxiliary arrays are created
All operations are swaps within the original array
Space complexity is O(log n) for recursion stack
No additional space proportional to input size
"""




# Exercise 4: Merge Sort with Custom Comparison
def merge_sort_with_compare(arr, key=None, reverse=False):
    if len(arr) <= 1:
        return arr
        
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            left_val = key(left[i]) if key else left[i]
            right_val = key(right[j]) if key else right[j]
            
            if (left_val <= right_val) != reverse:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    mid = len(arr) // 2
    left = merge_sort_with_compare(arr[:mid], key, reverse)
    right = merge_sort_with_compare(arr[mid:], key, reverse)
    return merge(left, right)

# Which statements are true?

# A. The implementation maintains stability even when using a key function
# B. Setting reverse=True will sort the array in descending order
# C. The implementation creates new arrays instead of sorting in-place
# D. The key function is called O(n log n) times during the sort
"""
A. True - Maintains stability because:

Equal elements maintain their relative order
The merge operation preserves order when values are equal
This holds true even with custom key functions
Left subarray elements are chosen first when equal

B. True - reverse=True leads to descending order:

The comparison condition is inverted
Changes <= to > in merge operation
Maintains stability while reversing order
Works correctly with custom key functions

C. True - Creates new arrays:

Not an in-place sort
Creates temporary arrays during merging
Space complexity is O(n)
Trade-off for stability and simplicity

D. True - Key function called O(n log n) times:

Each element is compared log n times on average
Key function is called for each comparison
Total number of comparisons is O(n log n)
Could be optimized by caching key values
"""
















# Exercise 5: Selection Sort with Binary Search Optimization
def optimized_selection_sort(arr):
    def binary_search_insert(sub_arr, target):
        left, right = 0, len(sub_arr)
        while left < right:
            mid = (left + right) // 2
            if sub_arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        if min_idx != i:
            insert_pos = binary_search_insert(arr[:i], arr[min_idx])
            temp = arr[min_idx]
            arr[insert_pos+1:min_idx+1] = arr[insert_pos:min_idx]
            arr[insert_pos] = temp
            
    return arr

# Which statements are true?

# A. The binary search optimization reduces the time complexity to O(n log n)
# B. The implementation maintains stability for equal elements
# C. The algorithm performs fewer swaps than standard selection sort
# D. The binary search is used to find the correct insertion position in the sorted portion


"""
Exercise 5: Selection Sort with Binary Search Optimization
Statement Analysis:
A. False - Still O(n²) because:

Still needs to find minimum element in unsorted portion
Binary search only optimizes insertion
Finding minimum still requires scanning unsorted portion
Cannot reduce below O(n²) without changing core algorithm

B. False - Not stable because:

Elements are moved in bulk during insertion
Original order of equal elements not preserved
Shifting elements changes relative positions
Would need additional complexity to maintain stability

C. True - Fewer swaps than standard selection sort:

Only one element moved to final position per iteration
Bulk movement is more efficient than multiple swaps
Elements shifted rather than swapped individually
However, doesn't improve overall time complexity

D. True - Binary search finds insertion position:

Used to locate where minimum element belongs in sorted portion
Reduces number of comparisons for insertion
More efficient than linear search for insertion
Particularly beneficial for large sorted portions
"""