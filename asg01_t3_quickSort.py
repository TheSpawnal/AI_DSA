
T3:Include Past Data with one Warehouse and Sort by Job Priority 
Covid happens and IKEA is in turmoil, as the way they were calculating the job priority (the constant selection time) does not work anymore. You have a bunch of jobs to schedule on a single ‘machine’.
Job j requires p j units of processing time and has a positive weight w j which represents its relative importance - think of it as the inventory cost of storing the raw materials for job j for 1 unit of time. If job j finishes being processed at time t, then it costs t * w j dollars. The goal is to sequence the jobs
so as to minimize the sum of the weighted completion times of each job. You should expect between 10*10K - 20*20K elements.
Use Smith’s rule, that is, schedule the jobs in the order of their ratio of processing time to weight.
This greedy rule turns out to be optimal.

Example 3. The sort() function takes a data list of tuples (list[tuple[id:int, p:int, w:int]])
as a parameter representing the data-set of jobs. Where, id, p, w are of type unsigned int, and, n is the number of orders.

<(i d1>, <p1>, <w1>), ..., (<i dn >,<pn >, <wn >)]

The function returns a list of integers of the job ids, sorted using Smith’s rule.
Hint: The Merge or Bubble sort may not work for this input size, consider Quick sort

template:
from typing import Optional, List, Tuple, Union

class Job:
    def __init__(self, id: int, p: int, w: int, next: Optional["Job"] = None):
        self.id: int = id
        self.p:  int = p
        self.w:  int = w
        '''
        Remove me if you don't need me.
        Or, add a method to assign to me if you want to use linked lists.
        '''
        self.next: Union[Job, None] = next
    '''
    Make your life easier and your code prettier, use `Operator Overloading`.
    '''
def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    '''
    Schedule (sort) the list of jobs using Smith's rule

    ### Parameters
    `data`: List of jobs represented as tuples
        `[(job_id, p, w), ...]`

    ### Return
    A list of the ids of the sorted jobs
    '''
    for id, p, w in data:
        # assert (isinstance(id, int) and isinstance(p, int)
        #         and isinstance(w, int))
        job: Job = Job(id, p, w)
        '''
        TODO: Append the `job` object to your structure.
        '''
        raise NotImplementedError
    '''
    TODO: Implement your schedule sorting function and add the params you need
            Use smith's rule to schedule.
    '''
    raise NotImplementedError
    '''
    TODO: Return a list of **integers** of the id's of the sorted list (Job.id).
            i.e: [1, 2, 3, 4, 5, 6]
    '''
    return None



 1 Define swap(arr, i, j)
 2      Swap objects between the indexes i and j of the arr list
 3
 4 Define quicksort(arr, lo, hi)
 5      If lo and hi are greater or equal to 0 and if lo is less than hi
 6      Partition the array
 7      Call the quicksort on the right partition
 8      Call the quicksort on the left partition
 9
 10 Define partition(arr, lo, hi)
 11     Pivot object is the object in the middle of the list
 12
 13     Set one counter (i) to the index before the lower index
 14     Set one counter (j) to the index after the upper index
 15
 16     Loop forever
 17         Update i by decreasing it by one
 18         While the value in arr at index i is less than the pivot
 19             Increase i (so that we are consider the next element in arr)
 20         Update j by decreasing it by one
 21         While the value in the arr at index j is greater that the pivot
 22             Increase j (so that we are consider the previous element in arr)
 23
 24         If the indexes i and j have crossed (i>=j) then return j
 25
 26         Swap the element at index i with the one at index j
 27
 28 Define sort(data)
 29     Create an empty support list
 30
 31     Fill the support list with the objects in data, converting them into an Order object
 32
 33     Call quicksort on the list
 34
 35     Return the id of every Order in the list


 1 def swap(arr: List[Order], i: int, j: int):
 2      arr[i], arr[j] = arr[j], arr[i]
 3
 4 def quicksort(arr: List[Order], lo: int, hi: int):
 5      if lo>= 0 and hi>= 0 and lo<hi:
 6      p = partition(arr, lo, hi)
 7      quicksort(arr, p + 1, hi)
 8      quicksort(arr, 0, p)
 9
 10 def partition(arr: List[Order], lo: int, hi: int):
 11     pivot = arr[(hi+lo)//2]
 12
 13     i = lo # initialize after lower bound :i = lo -1 
 14     j = hi # initialize after upper bound : j = hi + 1
 15
 16     while(True):
 17
 18         i = i + 1
 19         while arr[i]<pivot:
 20             i = i + 1
 21
 22         j = j−1
 23         while arr[j]>pivot:
 24             j = j−1
 25
 26         if i>= j:
 27             return j
 28
 29         swap(arr, i, j)
 30
 31
 32 def sort(data: List[Tuple[int,int,int]])−>List[int]:
 33     arr: List[Order] = []
 34
 35     for id, selectiont, shipping t in data:
 36         arr.append(Order(id, selectiont, shipping t))
 37
 38     quicksort(arr, 0, len(arr)−1)
 39
 40     return [a.id for a in arr]


which of the following statements about the code are true:

The implementation is correct and contains no bug.
FALSE

At line 2, the value swap between two variables cannot be done in that manner. It is necessary to rely on a temporary variable.
FALSE
 As previously mentioned: in python we are allowed to use this kind of object swap without
 relying on support variables. Due to the order the expression is evaluated, in the assignment
 cases python always evaluates the right-hand side of the expression first.

At lines 12 and 13, the i and j indices should be initialized as i = lo - 1 and j = hi + 1.
TRUE
 The i and j variables need to be set to i = lo-1 and j = hi+1 since once in the loop they
 will be respectively increased and decrease at every step to move towards the center. Since
 we want a single loop to run instead of one loop for the first step and a second loop for all
 the other steps, we need to set the variable to that ”correct” values. It is a simple coding
 trick that allows us to have a single loop, it is not really something specific about quicksort.
 If they are set to i = lo and j = hi then the first and last value will not be checked since
 in the while loop those values are then increased and decreased.

At lines 12 and 13, the i and j indices should be initialized as i = lo + 1 and j = hi - 1.
FALSE

At line 11, the pivot should be set as pivot = arr[lo], else the algorithm will not be able to sort correctly.
FALSE
The pivot of the array can be any element in the array. The best pivot point would be the
 one that has items that are less than itself on the left, and greater than itself items on the
 right. The middle point of the array is often used as pivot since reduces the cases in which
 all the elements needs to be moved (if you pick the first item as pivot you’ll have to move
 many elements unless the pivot you picked is the smallest number). But any index can be
 picked as pivot, non affecting the correctness of the final solution.