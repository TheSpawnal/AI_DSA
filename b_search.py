
LinearSearch(array, int x, int size){
    for i = 0 to size-1 do
        if(array[i] == x) then
            return i
    return -1    // Element not found
}


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
