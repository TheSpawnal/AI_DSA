QuickSort without In-Place Sorting: 
The code implements a variant of QuickSort that doesn't perform in-place sorting. 
In-place sorting would involve swapping elements within the original list to sort them, 
while this implementation creates new lists for smaller and greater elements.
Trade-offs: The non-in-place approach might be easier to understand and implement, 
but it's less memory-efficient as it creates additional lists. 
In-place sorting, while potentially more complex to implement, is more memory-efficient.


 Pseudocode
 1 Define swap(arr, i, j)
 2      Swap values of arr at index i and j
 3
 4 Define quicksort(ar)
 5      If there is one or less elements return ar
 6
 7      Pick the middle element as pivot
 8      Create two empty lists, one for objects smaller and one for objects greater than the pivot
 9      If you are analyzing the pivot then skip to the next object in list
 10     Put elements greater or same as the pivot in the list for the greater objects
 11     Put elements smaller than the pivot in the list fot the smaller objects
 12
 13     Set as the left list the quicksorted list with objects smaller than the pivot
 14     Set as the right list the quicksorted list with objects greater than the pivot
 15     Return the left list, appending the pivot, appending the right list


 1 def swap(arr: List[Order], i: int, j: int):
 2      tmp = arr[i]
 3      arr[i] = arr[j]
 4      arr[j] = tmp
 5
 6 def quicksort(ar: List[Order]):
 7
 8      if len(ar)<= 1:
 9      return ar
 10
 11     mid = len(ar)//2
 12     pivot = ar[mid]
 13
 14     smaller,greater = [],[] # missing : equal = []
 15
 16     for i, val in enumerate(ar):
 17         if i == mid:
 18             continue
 19         if val<pivot:
 20             smaller.append(val)
 21         elif val>pivot:
 22             greater.append(val)
#           else:
#               equal.append(val)            
 23
 24     left = quicksort(smaller)
 25     right = quicksort(greater)
 26     return left+[pivot]+right

which of the following statements about the code are true:

The implementation is correct and contains no bug.

The case of val == pivot is not specified, 
for this reason all the values equal to the pivot will be lost at every iteration.

The pivot is not included in the left sub-list nor the right sub-list, 
therefore its value will be lost during the execution.

The variable mid defined at line 11 may be a decimal number when len(arr) is an odd number. 
Thus causing the code to fail, since we cannot use a decimal value as an array index.