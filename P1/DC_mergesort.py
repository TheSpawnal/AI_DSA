""""
The code implements the Order class just like in the previous example. We did not copy the Order
class implementation, you can assume it s correct. The difference from the previous TaskOrder
implementation is that there is a Order.next field in this class which represents the following Order
(a pointer to the next element, just like in linked lists). The code implements a bottom-up merge
sort. The final sort method used in the previous Task code has been omitted, focus on the core
merge sort algorithm instead.


 Pseudocode
#Assume that the objects have a .next field that represent the following element, None if theres none
Define merge sort(head)
    if head is empty return None
    arr = list of 32 Nones
    result, next = None
    result = head

#Merge nodes into array
    while result is not null:
    Save the reference to the result next node into next
    Reset the result to None
    For each value of arr
        If current value is None then break
        result = merge(current value, result)
        Assign null to current value
    Assign result to the second last value of arr
    result = next

#Merge array into single list
    result = null
    For each item in arr
        result = merge(current value, result)

    return result

Define merge(left, right)
    result = None
    ref = None

    While left is not null and right is not null:
        If right greater or equal to left
            If result is not null then append left to the result
            else assign left to the result
            Assign the value after left to left
        else
            If result is not null then append right to the result
            else assign right to the result
            Assign the value after right to right

    While there are elements remaining in left
        Append left to result
        Assign the value after left to left

    While there are elements remaining in right
        Append right to result
        Assign the value after right to right

    Return the pointer to the start of the list
"""

class Order:
    def init (self, id, selectiontime, shippingtime):
        self.id: int = id
        self.selectiontime: int = selectiontime
        self.shippingtime: int = shippingtime
 
    def eq (self, other):
        return (self.selectiontime + self.shippingtime) == (other.selectiontime + other.shippingtime)
 
    def gt (self, other):
        return (self.selectiontime + self.shippingtime)>(other.selectiontime + other.shippingtime)

def merge sort(head: Union[Order,None])->Union[Order,None]:
    if not head:
        return None
    arr: List[Union[Order,None]] = [None for in range(32)]
    result: Union[Order,None] = None
    next: Union[Order,None] = None
    result = head
 
    while result:
        next = result.next
        result.next = None
        i = 0
        for i in range(32):
            if arr[i] is None:
                break #line 15
            result = merge(arr[i], result)
            arr[i] = None
 
        arr[i] = result
        result = next
 
    result = None
    for i in range(32):
        result = merge(arr[i], result)
 
    return result
  
def merge(left: Union[Order,None], right: Union[Order,None])−>Union[Order,None]:
    result: Union[Order,None] = None
    ref: Union[Order,None] = None

    while left and right:
        if left<= right:
            if result: #line 35
                result.add next(left)
                result = left
            else:
                ref = left
                result = left

            left = left.next
            
        else:
            if result:
                result.add next(right)
                result = right
            else:
                ref = right
                result = right

            right = right.next

    while left:
        if result:
            result.add next(left)
            result = left
        else:
            ref = left
            result = left

        left = left.next

    while right:
        if result:
            result.add next(right)
            result = right
        else:
            ref = right
            result = right

        right = right.next

    return ref


which are true: 
-At line 15, we should not break but instead return result, otherwise the code will never return once we are at the end.
-The implementation is correct and contains no bug.
-The code will only run for array of length divisible by 32.
-At line 35 we cannot use while left and right: since they are lists and will never have True or False as a value.

• We need the break because we need to move on since we reached the end of the array.
Returning at the point in time would not guarantee that the list got sorted. Break allows
us to exit the for loop.
• This represents an indeed correct implementation of merge sort.
• The code simply partitions the list in sublist of max 32 elements, the code will work even if
the last sublist has more than 32 elements, making this code effective also for lists with a
length not divisible by 32.
• All collection objects in python (lists, dictionaries, sets...) have a boolean value which is
determined by having or not elements in it. Their boolean value will be true if they have
at least one element in them. In this case the loop goes on as long as both left and right
have at least one element in each of them.