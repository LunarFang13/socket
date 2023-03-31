from collections import defaultdict
 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def isCycle(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
 
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCycle(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 

        recStack[v] = False
        return False
 
    def find_cycle(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCycle(node,visited,recStack) == True:
                    return True
        return False


# input from user

n = int(input("Enter the number of processes"))

wfg = Graph(n)

n = int(input("Enter the number of edges"))

for j in range(n):
    u, v = map(int, input("Enter the edge (a->b) :").split())
    wfg.addEdge(u, v)


if wfg.find_cycle():
    print('Deadlock detected')
else:
    print('No Deadlock')