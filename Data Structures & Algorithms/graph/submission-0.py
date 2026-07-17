class Graph:
    
    def __init__(self):
        self.adjList={}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src]=[]
        if dst  not in self.adjList:
            self.adjList[dst]=[]
        if dst not in self.adjList[src]:
            self.adjList[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False
        elif dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        else:
            return False
        


    def hasPath(self, src: int, dst: int) -> bool:
        visit=set()
        queue=deque()
        visit.add(src)
        queue.append(src)
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if node==dst:
                    return True
                for neighbor in self.adjList[node]:
                    if neighbor not in visit:
                        queue.append(neighbor)
                        visit.add(neighbor)
        return False

