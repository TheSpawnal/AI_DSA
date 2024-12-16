
T2:
our sorting program is successful, IKEA asks for your solution to run for several IKEA warehouses. We
should expect between 10*10K - 20*20K elements.
Hint: Bubble sort may not work anymore, consider Merge sort.

The sort() function has the same parameter/return format as:
Example2:
The sort() function takes a data list of tuples (list[tuple[id:int, t_selection:int,
t_shipping:int]]) as a parameter representing the data-set of orders. Where, id, t_selection and
t_shipping are of type unsigned int, and, n is the number of orders.
[(<id1>, <t_selection1>, <t_shipping1>),..., (<idN >, <t_selectionN >, <t_shippingN >)]
The function returns a list of integers of the order ids, sorted by t_selection + t_shipping.


template:
#!/usr/bin/env python3
from typing import Optional, List, Tuple, Union

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int,
                 next: Optional["Order"] = None):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        '''
        Remove me if you don't need me.
        Or, add a method to assign to me if you want to use linked lists.
        '''
        self.next: Union[Order, None] = next
    '''
    Make your life easier and your code prettier, use `Operator Overloading`.
    '''


def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    '''
    Sort the list of orders by `selection_time + sorting_time`
    ### Parameters
    `data`: List of orders represented as tuples
        `[(order_id, selection_time, shipping_time), ...]`
    ### Return
    A list of the ids of the sorted orders
    '''

    for id, selection_t, shipping_t in data:
        # assert (isinstance(id, int) and isinstance(selection_t, int)
        #         and isinstance(shipping_t, int))

        order: Order = Order(id, selection_t, shipping_t)
        '''
        TODO: Append the `order` object to your structure.
        '''
        raise NotImplementedError
    '''
    TODO: Perform the actual sorting of the orders
    '''
    raise NotImplementedError
    '''
    TODO: Return a list of **integers** of the id's (Order.id) of the sorted list.
            i.e: [1, 2, 3, 4, 5, 6]
    '''
    return None

'''
Use for your local testing
'''
# if __name__ == '__main__':
#     data = [(1, 500, 100), (2, 700, 100), (3, 100, 100)]
#     sort(data)
 
hints
1/Consider the format of the data for each task. Ask yourself the following questions by looking at the sample tests and task descriptions.
• Is the data ordered? partially ordered? or unordered?
• Does the task require the algorithm to be stable?
2/Perform floating point operations/comparisons to find the proper ordering.



Pseudo code:
 1 #Assume that the objects have a .next field that represent the following element, None if there’s none
 2
 3 Define merge sort(head)
 4 if head is empty return None
 5
 6 arr = list of 32 Nones
 7 result, next = None
 8
 9 result = head
 10
 11 #Merge nodes into array
 12 while result is not null:
 13 Save the reference to the result next node into next
 14 Reset the result to None
 15 For each value of arr
 16 If current value is None then break
 17 result = merge(current value, result)
 18 Assign null to current value
 19 Assign result to the second last value of arr
 20 result = next
 21
 22 #Merge array into single list
 23 result = null
 24 For each item in arr
 25 result = merge(current value, result)
 26
 27 return result
 28
 29 Define merge(left, right)
 30 result = None
 31 ref = None
 32
 33 While left is not null and right is not null:
 34 If right greater or equal to left
 35 If result is not null then append left to the result
 36 else assign left to the result
 37 Assign the value after left to left
 38 else
 39 If result is not null then append right to the result
 40 else assign right to the result
 41 Assign the value after right to right
 42
 43 While there are elements remaining in left
 44 Append left to result
 7
45 Assign the value after left to left
 46
 47 While there are elements remaining in right
 48 Append right to result
 49 Assign the value after right to right
 50
 51 Return the pointer to the start of the list


