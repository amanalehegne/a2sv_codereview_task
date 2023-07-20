from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]  # Special case for when there is only one node or no nodes
        
        graph = defaultdict(list)
        indegree = [0] * n
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegree[node1] += 1
            indegree[node2] += 1
        
        queue = deque()
        
        for node in range(n):
            if indegree[node] == 1:
                queue.append(node)
        
        while n > 2:
            size = len(queue)
            n -= size
            
            for _ in range(size):
                node = queue.popleft()
                children = graph[node]
                
                for child in children:
                    indegree[child] -= 1
                    
                    if indegree[child] == 1:
                        queue.append(child)
        
        return list(queue)
