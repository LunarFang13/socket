from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
 
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
    
    def combine(s1, s2):
        s3 = Graph(s1.V + s2.V)
        for i in s1.graph: 
            for j in s1.graph[i]:
                s3.addEdge(i, j)
        for i in s2.graph:
            for j in s2.graph[i]:
                s3.addEdge(i, j)
        return s3

 
    def find_cycle(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCycle(node,visited,recStack) == True:
                    return True
        return False


# input from user

wfgs = []

n = int(input("Enter the number of processes "))

s = int(input("Enter the number of sites "))

for i in range(s):
    wfgs.append(Graph(n))




for i in range(s):
    n = int(input("Enter the number of edges "))
    for j in range(n):
        u, v = map(int, input("Enter the edge (a->b) :").split())
        wfgs[i].addEdge(u, v)

def detect_deadlock(site_list):
        count = 1
        while len(site_list) > 1:
            count += 1
            local_cordinator = []
            for i in range(0, len(site_list), 2):
                if i+1 < len(site_list):
                    local_cordinator.append(Graph.combine(site_list[i], site_list[i+1]))
                    print(local_cordinator[len(local_cordinator)-1].graph)
                else:
                    local_cordinator.append(site_list[i])

            for i in local_cordinator:
                if Graph.find_cycle(i):
                    print("Deadlock detected in level-",count)
                    return
            site_list = local_cordinator
        print("No deadlock detected")

flag = 1
for wfg in wfgs:
    if wfg.find_cycle():
        print('Deadlock detected in level 1')
        flag = 0
    else:
        print('No Deadlock in level 1')
if flag:
    detect_deadlock(wfgs)