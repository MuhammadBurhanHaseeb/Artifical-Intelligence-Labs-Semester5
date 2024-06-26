import heapq

def A_Star_Search(graph, start, goal , heuristic):
    visited = set()
    priorityQueue = [(0, start,[])]
    while priorityQueue:
        (cost, node,path) = heapq.heappop(priorityQueue)
        if node not in visited:
            path = path + [node]
            visited.add(node)
            if node == goal:
                return cost ,path 
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priorityQueue, (cost + graph[node][neighbor] + heuristic[neighbor], neighbor,path))
    return float('inf')
    

graph = {'A': {'B': 1, 'C': 2},
         'B': {'A': 1, 'C': 3, 'D': 4},
         'C': {'A': 2, 'B': 3, 'D': 1},
         'D': {'B': 4, 'C': 1}}

heuristic = {'A': 10, 'B': 8, 'C': 5, 'D': 0}

min_cost,path = A_Star_Search(graph, 'A', 'D' , heuristic)
if min_cost == float('inf'):
    print("No path from 'A' to 'D")
else:
    print(f"Minimum cost from 'A' to 'D: {min_cost,path}")
