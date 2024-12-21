
# T2:
# our sorting program is successful, IKEA asks for your solution to run for several IKEA warehouses. We
# should expect between 10*10K - 20*20K elements.
# Hint: Bubble sort may not work anymore, consider Merge sort.
# The sort() function has the same parameter/return format as:
# Example2:
# The sort() function takes a data list of tuples (list[tuple[id:int, t_selection:int,
# t_shipping:int]]) as a parameter representing the data-set of orders. Where, id, t_selection and
# t_shipping are of type unsigned int, and, n is the number of orders.
# [(<id1>, <t_selection1>, <t_shipping1>),..., (<idN >, <t_selectionN >, <t_shippingN >)]
# The function returns a list of integers of the order ids, sorted by t_selection + t_shipping.


 
# hints
# 1/Consider the format of the data for each task. Ask yourself the following questions by looking at the sample tests and task descriptions.
# • Is the data ordered? partially ordered? or unordered?
# • Does the task require the algorithm to be stable?
# 2/Perform floating point operations/comparisons to find the proper ordering.



Pseudo code:
 1 #Assume that the objects have a .next field that represent the following element, None if there’s none
 2
 3 Define merge sort(head)
 4      if head is empty return None
 5
 6      arr = list of 32 Nones
 7      result, next = None
 8
 9      result = head
 10
 11     #Merge nodes into array
 12     while result is not null:
 13         Save the reference to the result next node into next
 14         Reset the result to None
 15         For each value of arr
 16             If current value is None then break
 17             result = merge(current value, result)
 18             Assign null to current value
 19         Assign result to the second last value of arr
 20         result = next
 21
 22      #Merge array into single list
 23     result = null
 24     For each item in arr
 25         result = merge(current value, result)
 26
 27     return result
 28
 29 Define merge(left, right)
 30     result = None
 31     ref = None
 32
 33     While left is not null and right is not null:
 34         If right greater or equal to left
 35             If result is not null then append left to the result
 36             else assign left to the result
 37             Assign the value after left to left
 38         else
 39             If result is not null then append right to the result
 40             else assign right to the result
 41             Assign the value after right to right
 42
 43     While there are elements remaining in left
 44         Append left to result
 45         Assign the value after left to left
 46
 47     While there are elements remaining in right
 48         Append right to result
 49         Assign the value after right to right
 50
 51     Return the pointer to the start of the list


 10 def merge_sort(head: Union[Order,None])->Union[Order,None]:
 20     if not head:
 30         return None
 40     arr: List[Union[Order,None]] = [None for _ in range(32)]
 50     result: Union[Order,None] = None
 60     next: Union[Order,None] = None
 70     result = head
 80
 90     while result:
 10         next = result.next
 11         result.next = None
 12         i = 0
 13         for i in range(32):
 14             if arr[i] is None:
 15                 break
 16             result = merge(arr[i], result)
 17             arr[i] = None
 18
 19         arr[i] = result
 20         result = next
 21
 22     result = None
 23     for i in range(32):
 24         result = merge(arr[i], result)
 25
 26     return result
 27
 28
 29 def merge(left: Union[Order,None], right: Union[Order,None])−>Union[Order,None]:
 30     result: Union[Order,None] = None
 31     ref: Union[Order,None] = None
 32
 33     while left and right:
 34         if left <= right:
 35             if result:
 36                 result.add_next(left)
 37                 result = left
 38             else:
 39                 ref = left
 40                 result = left
 41
 42             left = left.next
 43
 44         else:
 45             if result:
 46                 result.add_next(right)
 47                 result = right
 48             else:
 49                 ref = right
 50                 result = right
 51
 52             right = right.next
 53
 54     while left:
 55         if result:
 56             result.add_next(left)
 57             result = left
 58         else:
 59             ref = left
 60             result = left
 61
 62         left = left.next
 63
 64     while right:
 65         if result:
 66             result.add next(right)
 67             result = right
 68         else:
 69             ref = right
 70             result = right
 71
 72         right = right.next
 73
 74     return ref



which of the following statements about the code are true:

-At line 15, we should not break but instead return result, 
otherwise the code will never return once we are at the end.

-The implementation is correct and contains no bug.

-The code will only run for arrays of length divisible by 32.
   
-At line 35, we cannot use while left and right: 
   since they are lists and will never have True or False as a value.