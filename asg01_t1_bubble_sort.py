
T1:
Supply Chain Management Software at IKEA(Let's pretend).
IKEA has finally decided to invest in digitising their operations and the supply chain. 
They contracted us to design an algorithm to sort a list of orders by selection time (t_selection, finding the good in
the warehouse and bringing it to the surface) plus shipping time (t_shipping, constant). The customer
orders can be retrieved (in the same order as placed) from a server database. You should expect between
100-10K elements.
Hint: Bubble sort may do the job.
Example 2. The sort() function takes a data list of tuples (list[tuple[id:int, t_selection:int,
t_shipping:int]]) as a parameter representing the data-set of orders. Where, id, t_selection and
t_shipping are of type unsigned int, and, n is the number of orders.
[(<id1>, <t_selection1>, <t_shipping1>),..., (<idN >, <t_selectionN >, <t_shippingN >)]
The function returns a list of integers of the order ids, sorted by t_selection + t_shipping.

Call: sort([(1, 500, 100), (2, 700, 100), (3, 100, 100)])
Returns (list[int]): [3, 1, 2]


1.2 Task1:Bubblesort
 The code implements theOrder class. An Order will contain 3 fields: id,selectiontime,
 shippingtime.The=,<,>operators have been overloaded.A bubble sortalgorithm has been
 implemented, the bubble sort algorithm is wrapped in the sort method that parses the data and
 creates Order objects to pass to thebubblesort core method.

 Pseudocode
 1  Define Order class
 2  Define init(id, selection time, shipping time)
 3  Assign id to field id
 4  Assign selection time to field selection time
 5  Assign shipping time to field shipping time
 6  Define eq(other)
 7  Return true if this object and other object have same fields value else false
 8  Define gt(other):
 9  Return true if this object fields sum is greater than other object fields sum else false
 10
 11 Define bubbleSort(array)
 12 for each item in the array with i being the current index
 13 for each element but the last i
 14 swap current element with the following if the following is smaller than the current
 15
 16 Define sort(data)
 17 for each triplet in data
 18 append order initialized with the triplet to the array
 19 bubbleSort(array)
 20
 21 return list of [id of each order in array]

 1 class Order:
 2      def init (self, id, selectiontime, shippingtime):
 3          self.id: int = id
 4          self.selectiontime: int = selectiontime
 5          self.shippingtime: int = shippingtime
 6
 7      def eq (self, other):
 8          return (self.selectiontime + self.shippingtime) == (other.selectiontime + other.shippingtime)
 9
 10     def gt (self, other):
 11         return (self.selectiontime + self.shippingtime)>(other.selectiontime + other.shippingtime)
 12
 13
 14 def bubbleSort(array: List[Order]):
 15     n = len(array)
 16
 17     for i in range(n−1): # for i in range(n):
 18
 19         for j in range(1, n−i−1): # for j in range (0, n-i-1)
 20
 21             if array[j] > array[j+1]:
 22                 array[j], array[j+1] = array[j+1], array[j]
 23
 24 def sort(data: List[Tuple[int,int,int]])−>List[int]:
 25     arr: List[Order] = []
 26
 27     for id, selectiont, shipping t in data:
 28         arr.append(Order(id, selectiont, shipping t))
 29
 30     bubbleSort(arr)
 31
 32     return [a.id for a in arr]


 which of the following statements about the code are true:

On line 17, range(n-1) prevents the i index from traversing all the elements, leaving the last element untouched. TRUE
The implementation is correct and contains no bugs.FALSE
The j index is misused since it avoids comparing the first item of the list with the second.
On line 22, a support variable should be used to swap the array values, otherwise the result could be non-deterministic.



 Solution

 • The range in python includes the first item (0 by default), but excludes the last item. Since
 the last item of a list has index = the length of the list-1, we have to pass the length of the
 list to range since it will not reach it, but we’ll stop at the length- 1, which is our last index.
 Using n-1 will therefore prevent the last element to be ever visited.
 • The implementation is not correct due to the errors highlighted in the previous and in the
 following points.
 • being j in the range(1, n-i-1) it will start from 1 instead of 0, causing the first element
 of the list to never be compared with the second.
 • Inpython we are allowed to use this kind of object swap without relying on support variables.
 Due to the order the expression is evaluated, in the assignment cases python always evaluates
 the right-hand side of the expression first


 Mechanics:

 Bubble Sort
BubbleSort (Array A):
    n=size of A
    for i=0 to n-1 do
        for j=0 to n-i-1 do
            # compare two adjacent elements
                if A[j] > A[j + 1] then
                    swap(A[j],A[j+1])

Starting from the beginning of the array, compare adjacent elements
If the first element is greater than the second, swap them
Move to the next pair of adjacent elements
After each pass through the array, the largest unsorted element "bubbles up" to its correct position
The process repeats, each time working with a smaller unsorted portion of the array

Time Complexity:
Worst Case: O(n²)
Occurs when array is sorted in reverse order
Requires maximum number of comparisons and swaps


Best Case: O(n)
Occurs when array is already sorted
Only requires one pass to confirm no swaps needed

Average Case: O(n²)
Typically performs similarly to worst case
Not efficient for large datasets

Space Complexity:
O(1) - In-place algorithm
Only needs a single additional variable for swapping elements

Key Characteristics:
Stable Sort: Maintains relative order of equal elements
In-place: Doesn't require extra space proportional to input size
Adaptive: Performance improves if data is partially sorted
Comparison-based: Uses element comparisons to determine order

Optimization Techniques:

Early Termination:
pythonCopydef bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:  # If no swapping occurred, array is sorted
            break
Advantages:

Simple to understand and implement
Requires minimal extra space
Stable sorting algorithm
Works well for small datasets
Easy to detect if array is sorted

Disadvantages:

O(n²) complexity makes it inefficient for large datasets
Not suitable for large datasets
More swaps required compared to insertion sort

Best Use Cases:

Educational purposes (learning about sorting algorithms)
Small datasets (< 50 elements)
Nearly sorted data
When code simplicity is preferred over efficiency
When stable sorting is required and space is a constraint
