"""

code computes the shortest distance between the start_id node and any other node in the graph. The algo used is dijkstra 

Pseudocode:
Define dijkstra(graph, start id)
    Create a distances dictionary, the values are the distance between the start id node and the key (a node id)
    Create a dictionary to store the parent of vertices found along the shortest path
    Create a queue for vertices
    For every vertex in the graph
        Set its parent to-1
        Add the node to the queue
        Set the distance to infinity for all nodes, start id distance set to 0
 
    While there are values in the queue
        Set the smallest known distance to infinity
        Set the node the distance refers to, to the next smallest node in the queue (later called the current node)
 
        The following for loop looks for the node with the shortest distance in the queue
        For every node in the queue
            If the distance between the start id and the node is less than the smallest known distance, then set the current node to this  node, together with its distance
        Remove the current node from the queue
 
        Now update the distances of the neihboring vertices passing by the current node
        For every neighbour of the current node that is still in the queue
            The distance from the neighbour to start id passing by the current node is the distance of the current node from start id + the distance of the current node and the neighbour
            If this new distance is lower than the previous distance of the neighbour from start id
                Then update the distance in the distances dictionary
                In the parents dictionary, set the current node as the current neighbor parent
 
    Return the distances and parent dictionaries
"""

def dijkstra(graph, start_id: int)->Tuple[dict, dict]:
    dist = {}
    parent = {}
    queue = []
    for v in graph:
        parent[v] =-1
        queue.append(v)
        dist[v] = float('inf') if v != start_id else 0
 
    while queue:
        u_val: float = float('inf')
        u: Node = queue[0]
        for q in queue:
            u_val, u = (dist[q.id], q) if dist[q.id]>u_val else (u_val, u)
        queue.remove(u)
 
        children = [i for i in u.children if i in queue]
        for v in children:
            alt = v.weight
            if alt<dist[v.id]:
                dist[v.id] = alt
                parent[v.id] = u.id
    return dist, parent

"""
which are true:

- the ifs: 
    dist[v] = float('inf') if v != start id else 0
    u_val, u = (dist[q.id], q) if dist[q.id]>u_val else (uval, u)
are not correct Python sytntax

- u_val, u = (dist[q.id], q) if dist[q.id]>u val else (u_val, u) 
a less than (<) should be used, since we want to get the node which distance is the shortest

- line 52: 
    alt = v.weight
the new distance should be dist[u.id]+ v.weight instead of only the last node wight(which is 
what we often call distance in this scenarios)

-this is a correct implemntation of dijktra algo


Solution

 • The syntax is indeed admitted, it is often called a ternary operator. It is just a shorthand
 for an if-else statement in python, just like in many other languages.

 • It is true, if we need to find the closest node to start
 id, we need to update u and u with a value that is less that the current distance, not greater.

 • The distances in the dist dictionary represent the distances from the start_id, therefore
 we need to get the distance to the previous point (u) plus the distance between u and v, in
 order to get the whole path from start_id to v.

 • Due to the 2 previous statements this is not a correct Dijkstra s algorithm implementation,
 by solving those two issues it would become one.

"""


#  Which of the following statement(s) are true:

#  Whenlooking for an element in a tree we must perform both a BFS and a DFS since the BFS
#  will look for the items at the same level of the starting point and the DFS will look for the
#  items on the branch starting from the starting point. Using only one of them may exclude
#  some items from the search.

#  Dijkstra’s algorithm can find the shortest path only for acyclical graphs, if cycles are in the
#  graph then we need to use A* that will instead follow its heuristic without being tricked into
#  the cycles. 

# √ Dijkstra’s algorithm runs on an unweighted graph (every edge has the same weight), works
#  just like a classic BFS search.
#  • BFS and DFS look for items within a tree. The way they operate is similar but they simply
#  follow different paths, DFS explores the tree vertically first while BFS explores it breadth
#  first. Regardless of the order they’ll both check out every element, so using one of them is
#  totally fine, we do not need to use both at the same time.
#  • Dijkstra’s algorithm works also in cyclical graphs, since it will not revisit the exact same
#  path twice. But it could visit the same node multiple times to try find a shorter path to it.
#  • Dijkstra’s algorithm works just like BFS when no difference in weights between the edges
#  is found. This is because Dijkstra is going to take the next node with the shortest distance
#  from the source. Dijkstra is essentially a BFS with respect to the edge weights rather than
#  the topology (BFS is guided by topology, not edge weights)