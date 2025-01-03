

def sequential_search(arr, x):
    # Handle empty array case
    if not arr:
        return -1
    
    # Iterate through each element
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    
    # Element not found
    return -1



#     Key characteristics of this implementation:

# Time Complexity: O(n) - it may need to check every element in the worst case
# Space Complexity: O(1) - uses only a constant amount of extra space
# Works on both sorted and unsorted arrays
# Returns -1 if element is not found (consistent with the binary search implementation)
# Returns the first occurrence of x if there are duplicates

# Compared to binary search:

# Simpler implementation
# Works with unsorted arrays
# Less efficient for large sorted arrays (O(n) vs O(log n))
# No need for the array to be sorted