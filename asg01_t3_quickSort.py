
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

