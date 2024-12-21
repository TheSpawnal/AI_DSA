Pseudocode:
CopyDefine binary_search(sorted_array, target_value)
    Set left = 0
    Set right = length of array - 1
    
    While left <= right:
        Set middle = (left + right) // 2
        
        If element at middle equals target_value:
            Return middle
        If element at middle < target_value:
            Set left = middle + 1
        Else:
            Set right = middle - 1
    
    Return -1 (element not found)

Define binary_search_order(sorted_orders, target_processing_time)
    Set left = 0
    Set right = length of orders - 1
    
    While left <= right:
        Set middle = (left + right) // 2
        current_processing_time = orders[middle].selection_time + orders[middle].shipping_time
        
        If current_processing_time equals target_processing_time:
            Return orders[middle].id
        If current_processing_time < target_processing_time:
            Set left = middle + 1
        Else:
            Set right = middle - 1
    
    Return -1 (no order with target processing time found)


Python Implementation:
pythonCopydef binary_search(array: List[Order], target_processing_time: int) -> int:
    """
    Search for an order with specific total processing time in sorted array
    Returns order ID if found, -1 if not found
    Assumes array is sorted by processing time (selection_time + shipping_time)
    """
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        current_time = array[mid].selection_time + array[mid].shipping_time
        
        if current_time == target_processing_time:
            return array[mid].id
        elif current_time < target_processing_time:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

Characteristics:
Time Complexity: O(log n)
Space Complexity: O(1)
Best for: Large datasets
Requires sorted array
Much faster than sequential search for large datasets

Key Differences:
Preprocessing Requirements:
Sequential Search: No preprocessing needed
Binary Search: Requires sorted array

Performance:
Sequential Search: Checks every element (O(n))
Binary Search: Halves the search space each time (O(log n))


Use Cases:

Sequential Search:

Small datasets
Unsorted data
One-time searches


Binary Search:

Large datasets
Frequently searched data
When preprocessing (sorting) cost is justified




Memory Usage:

Both use O(1) extra space
Binary search requires sorted array (initial preprocessing)
