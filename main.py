from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    heap = [(0, 0, source)]
    visited = {}

    while heap:
        weight, num_edges, u = heappop(heap)
        if u in visited:
            prev_weight, prev_edges = visited[u]
            if weight > prev_weight or (weight == prev_weight and num_edges >= prev_edges):
                continue
        visited[u] = (weight, num_edges)
        for v, w in graph.get(u, set()):
            heappush(heap, (weight + w, num_edges + 1, v))
    return visited

def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in graph.get(u, set()):
            if v not in parents:
                parents[v] = u
                queue.append(v)
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    while destination in parents:
        destination = parents[destination]
        if destination is None:
            break
        path.append(destination)
    path.reverse()
    return ''.join(path)
    
