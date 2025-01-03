
# Malfunctioning sensors:

# Unfortunately some of the sensors started to malfunction. 
# Presumably, they report the reading value more than once each day. 
# The water management department has pinned it down to the neighbour-hood De Pijp, 
# and a few suspicious measurements have been identified for you. 
# Since there is some time pressure to fix the problem, 
# your colleague has already sorted the measurements for you late last night. 
# Your task is to implement an algorithm that counts occurrences of a given number. 
# Of course, the array may contain duplicated values and the algorithm should 
# return 0 if it can not find any such occurrence.

# Example 2. The find_occurrences function takes two parameters:
# • array (list[int]): An sorted array of positive integers
# • n (int)
# The function returns an Integer representing the number of occurrences if found of n in array
# Call: find_occurrences([1, 1, 2, 3, 4, 4, 4, 8, 10], 1)
# Returns (int):2

# function template:
# from typing import List


# def find_occurrences(array: List[int], n: int
#                      ) -> int:
#     '''
#     Find the number of occurrences of `n` in the `array` list

#     ### Parameters
#     `array`: An  **ordered** array of positive integers

#     `n`: int

#     ### Return
#     The number of occurrences of `n` in `array`
#     '''

#     raise NotImplementedError


#modified binarySearch approach to fin both the first and last occurence of the target number:
from typing import List
def find_occurrences(array: List[int], n: int) -> int:
    '''
    Find the number of occurrences of `n` in the `array` list
    ### Parameters
    `array`: An  **ordered** array of positive integers
    `n`: int

    ### Return
    The number of occurrences of `n` in `array`
    '''
    # Find leftmost occurrence
    def find_first(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        first_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first_pos = mid
                # Continue searching in left half
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first_pos

    # Find rightmost occurrence
    def find_last(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        last_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last_pos = mid
                # Continue searching in right half
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last_pos

    # Get first and last positions
    first = find_first(array, n)
    last = find_last(array, n)
    
    # If number not found, return 0
    if first == -1:
        return 0
        
    # Return count of occurrences
    return last - first + 1



# simple binarySearch appoach: 
def find_occurrences(array: List[int], n: int) -> int:
    '''
    Find the number of occurrences of `n` in the `array` list

    ### Parameters
    `array`: An  **ordered** array of positive integers
    `n`: int

    ### Return
    The number of occurrences of `n` in `array`
    '''
    left, right = 0, len(array) - 1
    count = 0
    
    # Find any occurrence first
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == n:
            # Count outward from found position
            count = 1
            i, j = mid - 1, mid + 1
            
            # Count left duplicates
            while i >= 0 and array[i] == n:
                count += 1
                i -= 1
                
            # Count right duplicates
            while j < len(array) and array[j] == n:
                count += 1
                j += 1
                
            return count
        elif array[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
            
    return count