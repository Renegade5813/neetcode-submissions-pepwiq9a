from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #if cycle found, return []
        #start node cannot have prereq
        #use top sort to find first node
        #when you find first node, run dfs on prerequisites to find a path

        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        in_degree = [0] * numCourses  # Count of incoming edges for each vertex

        # Calculate in-degree for each vertex
        for u in adj:
            for v in adj[u]:
                in_degree[v] += 1

        # Queue for vertices with 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)

            # Decrease in-degree for adjacent vertices
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return topo_order if len(topo_order) == numCourses else []