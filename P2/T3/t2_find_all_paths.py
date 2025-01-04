'''
task :find all the possible paths from which a (TwitterID-A) could have seen a post by a user(TwitterID-B). 
For each path a vertice should be visited only once as the graph may contain cycles.
Allowed data structures 2: tuple, dict, list, set
Dataformat2. Thefind_paths()function takes the same parameters and data format as our first task1 findonepath. 
But, returns a list of lists (list[list[int]]) of all possible paths from start to end.
[ [idstart>, ..., <idend>], [<idstart>, ..., <idend>], ...]
Call: find_paths(1, 3, [(1, [2, 3]), (2, [3, 1]), (3, [2])])
Returns (list[list[int]]): [[1, 3], [1, 2, 3]]
'''

from typing import List, Tuple, Dict, Set

def find(graph: Dict[int, Set[int]], start: int, end: int, path: List[int], all_paths: List[List[int]]):
    path = path + [start]
    if start == end:
        all_paths.append(path)
    else:
        for node in graph.get(start, set()):
            if node not in path:
                find(graph, node, end, path, all_paths)

def find_paths(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]) -> List[List[int]]:
    """
    Find all paths between start_id and end_id in the given Twitter user data.
    Parameters:
    start_id : int
        ID of the starting node
    end_id : int
        ID of the target node
    data : list[tuple[int, list[int]]]
        List of tuples of the twitter user data (id:int, following:list[int])

    Returns:
    list[list[int]]: List of lists of the node ids as integers of all paths found between the start and end nodes
    """
    # Step 1: Create and store the graph
    graph: Dict[int, Set[int]] = {}
    for id, following in data:
        if id not in graph:
            graph[id] = set()
        for f in following:
            graph[id].add(f)
    
    # Step 2 & 3: Call the 'find' function with the created graph
    all_paths: List[List[int]] = []
    find(graph, start_id, end_id, [], all_paths)
    
    # Step 4: Return all paths found
    return all_paths