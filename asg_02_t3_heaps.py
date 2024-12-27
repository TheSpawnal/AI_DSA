Heaps are commonly implemented with an array, 
the positioning in the array determines the positioning in the tree, 
here's an example: [A,B,C,D,E,F] A has 2 leaves (BandC), 
B has 2 leaves (DandE), C has 1 leaf(F). 
Considering the lexicographical order this would be a min-heap since 
the children are always greater than the parent. 
Here's an implementation of min-heap and some of its main methods





#recall mainstrean implementation:
class MinHeap:
    def __init__(self):
        # Initialize with empty list
        self.heap = []
    
    def parent(self, i):
        # Get parent index
        return (i - 1) // 2
    
    def left_child(self, i):
        # Get left child index
        return 2 * i + 1
    
    def right_child(self, i):
        # Get right child index
        return 2 * i + 2
        
    def swap(self, i, j):
        # Helper to swap elements
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, key):
        # Add the new key at the end
        self.heap.append(key)
        # Fix the min heap property if violated
        self._sift_up(len(self.heap) - 1)
    
    def _sift_up(self, i):
        # Move the element up until heap property is satisfied
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
            
        # Store the minimum value
        min_val = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Fix the min heap property if violated
        if len(self.heap) > 0:
            self._sift_down(0)
            
        return min_val
    
    def _sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Compare with left child
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
            
        # Compare with right child
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
            
        # If min_index changed, we need to swap and continue sifting down
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)
    
    def get_min(self):
        # Return minimum element without removing it
        if len(self.heap) == 0:
            return None
        return self.heap[0]

# Example usage:
if __name__ == "__main__":
    heap = MinHeap()
    # Insert example from your description: [A,B,C,D,E,F]
    for char in ['A', 'B', 'C', 'D', 'E', 'F']:
        heap.insert(char)
    
    print("Initial heap:", heap.heap)
    print("Min element:", heap.get_min())
    print("Extracting elements in order:")
    while heap.heap:
        print(heap.extract_min(), end=' ')
