# Supply Chain Management Software at IKEA(Let's pretend).
# IKEA has finally decided to invest in digitising their operations and the supply chain. They contracted
# us to design an algorithm to sort a list of orders by selection time (t_selection, finding the good in
# the warehouse and bringing it to the surface) plus shipping time (t_shipping, constant). The customer
# orders can be retrieved (in the same order as placed) from a server database. You should expect between
# 100-10K elements.
# Hint: Bubble sort may do the job.
# Example 2. The sort() function takes a data list of tuples (list[tuple[id:int, t_selection:int,
# t_shipping:int]]) as a parameter representing the data-set of orders. Where, id, t_selection and
# t_shipping are of type unsigned int, and, n is the number of orders.
# [(<id1>, <t_selection1>, <t_shipping1>),..., (<idN >, <t_selectionN >, <t_shippingN >)]
# The function returns a list of integers of the order ids, sorted by t_selection + t_shipping.

# Call: sort([(1, 500, 100), (2, 700, 100), (3, 100, 100)])
# Returns (list[int]): [3, 1, 2]



from typing import Optional, List, Tuple, Union

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int,
                 next: Optional["Order"] = None):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time: int = shipping_time
        self.next: Union[Order, None] = next
        
    def __eq__(self, other: "Order") -> bool:
        if not other:
            return False
        return (self.selection_time + self.shipping_time) == (other.selection_time + other.shipping_time)
    
    def __gt__(self, other: "Order") -> bool:
        if not other:
            return True
        return (self.selection_time + self.shipping_time) > (other.selection_time + other.shipping_time)
    
    def __lt__(self, other: "Order") -> bool:
        if not other:
            return False
        return (self.selection_time + self.shipping_time) < (other.selection_time + other.shipping_time)

def bubble_sort_linked_list(head: Union[Order, None]) -> Union[Order, None]:
    """Bubble sort implementation for linked list of Orders"""
    if not head or not head.next:
        return head

    swapped = True
    while swapped:
        swapped = False
        curr = head
        prev = None
        
        while curr.next:
            if curr > curr.next:
                # Handle swapping
                next_node = curr.next
                curr.next = next_node.next
                next_node.next = curr
                
                if prev:
                    prev.next = next_node
                else:
                    head = next_node
                    
                swapped = True
                prev = next_node
            else:
                prev = curr
                curr = curr.next
                
    return head

def sort(data: List[Tuple[int, int, int]]) -> List[int]:
    """Sort orders by selection_time + shipping_time and return sorted ids"""
    if not data:
        return []
        
    # Create head of linked list
    head = Order(data[0][0], data[0][1], data[0][2])
    current = head
    
    # Build linked list
    for id, selection_t, shipping_t in data[1:]:
        current.next = Order(id, selection_t, shipping_t)
        current = current.next
    
    # Sort the linked list
    sorted_head = bubble_sort_linked_list(head)
    
    # Extract sorted ids
    result = []
    current = sorted_head
    while current:
        result.append(current.id)
        current = current.next
        
    return result