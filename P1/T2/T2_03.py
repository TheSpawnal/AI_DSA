# Checking for the right data structure:
# The cooperation between the water management and health authorities has been very successful , 
# the new covid measurement system is about to go online for every city in the Netherlands. 
# However, after a long discussion with your colleague, you both realized that some of the new 
# algorithms will not scale to the new amounts of readings you will have to handle. 
# In particular, the new algorithms include an enormous amount of calls to a function called "findmin". 
# You decided to implement a new data structure, and your colleague did a first attempt last week. 
# Since this is a huge opportunity, you both want to make sure the data structure was implemented correctly.
# You task is to implement an algorithm that checks it a given integer array represents a min-heap or not.

# Example 3. The is_min_heap function takes one parameters:
# • array (list[int]): An array of positive integers
# The function returns a Boolean or an Integer
# Call: is_min_heap([1, 2, 5, 3, 4, 6, 7])
# Returns (Union[int, bool]): 1 | True


from typing import List, Union

def is_min_heap(array: List[int]) -> Union[int, bool]:
    '''
    Determine if `array` represents a min heap

    ### Parameters
    `array`: An array of positive integers

    ### Return
    A boolean or int (0|1) for if the `array` is a min heap
    '''
    # Empty array or single element is considered a valid min heap
    if not array or len(array) == 1:
        return 1
    
    # For each parent node at index i
    # Left child: 2i + 1
    # Right child: 2i + 2
    for i in range(len(array) // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check left child exists and parent > left child
        if left < len(array) and array[i] > array[left]:
            return 0
            
        # Check right child exists and parent > right child
        if right < len(array) and array[i] > array[right]:
            return 0
    
    return 1