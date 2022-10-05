import math
import bisect
import collections
from typing import *;
adjlist1 = [[2,4],[1,3],[2,4],[1,3]]
adjlist=[[2],[1,4,7],[5],[2,6],[3],[4,7],[2,6]]
#1-2-3-4
adjlist2 = [[2],[1,3],[2,4],[3]]
adjlist4 = [[2],[1,3,7],[2,4],[3,5],[4,6,8],[5,7],[2,6],[5]] #bipartite
adjlist5 = [[2],[1,3,8],[2,4],[3,5],[4,6,8],[5,7],[6],[2,5]] #not bipartite

adjlist6 = [[2],[3],[4,6],[5],[],[5]]
adjlist = adjlist6.copy()
graph={}
for i in range(len(adjlist)):
    graph[i+1] = adjlist[i]

print(graph)
def dfsutil(i,visited):
    visited[i] = True
    print(i)
    for j in graph[i]:
        if visited[j] == False:
            dfsutil(j,visited)

def dfs():
    V= len(graph)+1
    visited = [False]* V
    for i in range(1,V):
        if visited[i] == False:
            dfsutil(i,visited)
#dfs()
def iterdfsutil(v,visited):
    s= collections.deque()
    s.append(v)
    while s:
        top = s.pop()
        if visited[top]:
            continue
        visited[top] = True
        print(top)
        for i in graph[top]:
            if not visited[i]:
                s.append(i)

def iterdfs():
    V = len(graph) + 1
    visited = [False] * V
    for i in range(1,V):
        if not visited[i]:
            iterdfsutil(i,visited)

#iterdfs()

def iterbfsutil(v,visited):
    q = collections.deque()
    visited[v] = True
    q.append(v)
    while q:
        front = q.popleft()
        print(front)
        for i in graph[front]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def iterbfs():
    V = len(graph) + 1
    visited = [False] * V
    for i in range(1,V):
        if not visited[i]:
            iterbfsutil(i,visited)

#iterbfs()

def bfsutil(q,visited):
    if not q:
        return
    front = q.popleft()
    print(front)
    for i in graph[front]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    bfsutil(q,visited)

def bfs():
    V = len(graph) + 1
    visited = [False] * V
    q = collections.deque()
    for i in range(1, V):
        if not visited[i]:
            q.append(i)
            visited[i] = True
            bfsutil(q,visited)

#bfs()
def cyclebfs(v:int,visited:List[bool])->bool:
    q = collections.deque()
    q.append([v,0])
    visited[v] = True
    #print(q)
    while q:
        front,prev = q.popleft()
        print(front)
        #print(graph[front])
        for i in graph[front]:
            if i != prev and visited[i]:
                return True
            if not visited[i]:
                visited[i]=True
                q.append([i,front])
                print([i,front])

def findcycle_bfs():
    v = len(graph) +1
    visited = [False]* v
    for i in range(1,v):
        if not visited[i]:
            if cyclebfs(i,visited):
                return True
    return False

#if findcycle_bfs():
#    print("contains cycle")
#else:
#    print("no cycle")


def cycledfs(v,visited):
    s = collections.deque()
    s.append([v,0])
    while s:
        top,prev = s.pop()
        print(top)
        if visited[top]:
            continue
        visited[top] = True
        for i in graph[top]:
            if i!=prev and visited[i]:
                return True
            if not visited[i]:
                s.append([i,top])

def findcycle_dfs():
    v = len(graph) + 1
    visited = [False] * v
    for i in range(1, v):
        if not visited[i]:
            if cycledfs(i, visited):
                return True
    return False

if findcycle_dfs():
    print("contains cycle")
else:
    print("no cycle")

def isbp_bfs(v,color):
    q = collections.deque([v])
    q.append(v)
    color[v] = False
    while q:
        front = q.popleft()
        for i in graph[front]:
            if color[i] == -1:
                q.append(i)
                color[i] = not color[front]
            else:
                if color[i] == color[front]:
                    return False
    print(color)
    return True


def bipartite_bfs():
    color = [-1]*(len(graph)+1)
    for i in range(1,len(color)):
        if color[i] == -1:
            if isbp_bfs(i,color):
                print("it's bipartite")
            else:
                print("it's not bipartite")
                return

#bipartite_bfs()
def isbp_dfs(v,color):
    if color[v]== -1:
        color[v] = False
    for i in graph[v]:
        if color[i] == -1:
            color[i] = not color[v]
            if not isbp_dfs(i,color):
                return False
        elif color[i] == color[v]:
            return False
    return True



def bipartite_dfs():
    color = [-1]* (len(graph)+1)
    for i in range(1,len(color)):
        if color[i] == -1:
            if isbp_dfs(i,color):
                print("It's bipartite")
            else:
                print("not bipartite")
                return

#bipartite_dfs()
def containscycle(v,visited,dfs_vis):
    visited[v] = 1
    dfs_vis[v] = 1
    for i in graph[v]:
        if not visited[i]:
            if containscycle(i,visited,dfs_vis):
                return True
            #dfs_vis[i] = 0
        elif dfs_vis[i]:
            return True
    dfs_vis[v] = 0
    return False

def findcycle_directed_dfs():
    visited = [0]* (len(graph)+1)
    dfs_vis = [0]* (len(graph)+1)
    for i in range(1,len(visited)):
        if not visited[i]:
            if containscycle(i,visited,dfs_vis):
                return True
    return False
if findcycle_directed_dfs():
    print("contains cycle")
else:
    print("no cycle detected")
