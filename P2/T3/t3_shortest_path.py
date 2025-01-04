
'''
develop an algorithm that finds the shortest path between  user(TwitterID-A) spreading fake news and someother user(TwitterID-B).
Allowed data structures 3: tuple, dict, list, set
Dataformat3. The shortest_path function takes three parameters: 
two integers representing the start and end node ids, and, 
the list of the twitter users with their number of likes and the users they arefollowing. 
Each twitter user(node)is given as a tuple(tuple[id:int, num_likes:int, following:list[int]]).
All edges directed to a node u have a weight of 1/num_likes_u
[ (<id1>, <num_likes1>, [<id1,1>, <id1,2>, ...]), ..., (<idn>, <num_likesn>,
[<idn,1>, <idn,2>, ...]) ]
The function returns a list of integer node_ids of the shortest paths between the start and end nodes.
[<idstart, ..., <idend>]
Call: shortest_path(1, 3, [(1, 2, [2, 3]), (2, 5, [3, 1]), (3, 6, [2])])
Returns (list[int]): [1, 3]
'''


from typing import List, Tuple, Dict
import heapq

class Node:
    def __init__(self, weight: int):
        self.weight = weight
        self.following = []

def dijkstra(graph: Dict[int, Node], start_id: int, end_id: int) -> List[int]:
    distances = {node: float('infinity') for node in graph}
    distances[start_id] = 0
    pq = [(0, start_id)]
    previous = {}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end_id:
            path = []
            while current_node in previous:
                path.append(current_node)
                current_node = previous[current_node]
            path.append(start_id)
            return path[::-1]

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node].following:
            weight = 1 / graph[neighbor].weight
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return []  # If no path is found

def shortest_path(start_id: int, end_id: int, data: List[Tuple[int, int, List[int]]]
                  ) -> List[int]:
    """
    Implement the dijkstra shortest path algorithm.
    Parameters:
    start_id : int
        ID of the starting node
    end_id : int
        ID of the target node
    data : list[tuple[int, int, list[int]]]
        List of tuples of the twitter user data
            (id: int, num_likes (weight): int, following: list[int])
        e.g. [(1, 2, [2, 3]), (2, 5, [3, 1]), (3, 6, [2])]

    Returns:
    list[int]: List node id as integers
        of the shortest path found between the start and end nodes.
    """
    # Create and store the graph
    graph = {}
    for id, num_likes, following in data:
        if id not in graph:
            graph[id] = Node(num_likes)
        graph[id].following.extend(following)
    # Call the dijkstra function with the parameters
    path = dijkstra(graph, start_id, end_id)
    # Return a list of integers of the node IDs of the shortest path
    return path

