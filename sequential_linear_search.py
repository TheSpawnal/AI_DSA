Pseudocode:
CopyDefine sequential_search(array, target_value)
    For each element in array from index 0 to length-1:
        If current element equals target_value:
            Return index of current element
    Return -1 (element not found)

Define sequential_search_order(orders, target_processing_time)
    For each order in orders from index 0 to length-1:
        If (order.selection_time + order.shipping_time) equals target_processing_time:
            Return order.id
    Return -1 (no order with target processing time found)

Python Imple:
pythonCopydef sequential_search(array: List[Order], target_processing_time: int) -> int:
    """
    Search for an order with specific total processing time
    Returns order ID if found, -1 if not found
    """
    for order in array:
        if (order.selection_time + order.shipping_time) == target_processing_time:
            return order.id
    return -1

Characteristics:
Time Complexity: O(n)
Space Complexity: O(1)
Best for: Small datasets, unsorted arrays
No preprocessing required
