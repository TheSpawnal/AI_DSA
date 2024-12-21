class Order:
    def __init__(self, id, selectiontime, shippingtime):
        self.id: int = id
        self.selectiontime: int = selectiontime
        self.shippingtime: int = shippingtime
    
    def gt(self, other):
        return (self.selectiontime + self.shippingtime) > (other.selectiontime + other.shippingtime)

def selectionSort(array: List[Order]):
    n = len(array)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # Find minimum element in remaining unsorted array
            if array[min_idx].gt(array[j]):
                min_idx = j
                
        # Swap the found minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]

def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    arr: List[Order] = []
    
    for id, selectiont, shippingt in data:
        arr.append(Order(id, selectiont, shippingt))
    
    selectionSort(arr)
    
    return [a.id for a in arr]



# selection sort analysis:

# SelectionSort(Array A)
# n = size of A
# for(i = 0; i <(n-1);i++)
#     index_min = i
#     for (j:=(i+1);j<n;j++)
#         if A[j] < A[i] then
#             index_min = j
#     swap(A[i], A[index_min])