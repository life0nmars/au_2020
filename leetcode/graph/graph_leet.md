+ [Course Schedule II](#course-schedule-ii)
+ [Number of Islands](#number-of-islands/discuss/1224560/DFS-Using-Pytho)
+ [Is Graph Bipartite?](#is-graph-bipartite/discuss/1224386/Clean-python-bfs-solutio)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)
<!-----solution----->

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
def maxDepth(self, root: 'Node') -> int:
    
    if root is None:
        return 0
    
    maxValue = 0
    for child in root.children:
        
        childHeight = self.maxDepth(child)
        maxValue = max(maxValue,childHeight)
        
    return 1+maxValue
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    n=len(grid)
    
    if grid[0][0] or grid[-1][-1]:
        return -1
    
    queue=[(0,0,1)]
    dir=[(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i,j,d in queue:
        if i==n-1 and j==n-1:
            return d
        
        for x,y in dir:
            row=i+x
            col=j+y
            
            if 0<=row<n and 0<=col<n and not grid[row][col]:
                queue.append((row,col,d+1))
                grid[row][col]=1
    
    return -1
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    g=defaultdict(list)
    for f,t,p in flights:g[f].append((t,p))
    M=defaultdict(int);q=[(src,0,0)];r=float('inf')
    while q:
        t,k,p=q.pop(0)
        if p>=r or k>K+1:continue
        if t==dst:r=min(r,p)
        for n,np in g[t]:
            if M[n]==0 or M[n]>p+np:M[n]=p+np;q.append((n,k+1,p+np))
    return r if r!=float('inf') else -1
```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/discuss/1224386/Clean-python-bfs-solution

```python
def isBipartite(self, graph: List[List[int]]) -> bool:
    # 0 - not colored
    # 1 - red color
    # 2 - blue color
    color = [0]*len(graph) # number of nodes in the graph
    
    for i in range(len(graph)): # this is required in case there are more than one disjoint graphs.
        if color[i] == 0:
            q = deque()
            q.append((i, 1)) # initially color is by red.
            while(q):
                node, ncolor = q.popleft() 

                if color[node] == 0: 
                    color[node] = ncolor 

                    for nx in graph[node]:
                        q.append((nx, -ncolor)) #assign opposite color

                if color[node] != ncolor: # if color you assigned is not equal to the curr color
                    return False
                    
    
    return True
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/discuss/1224560/DFS-Using-Python

```python
def numIslands(self, grid: List[List[str]]) -> int:
    def dfsHelper(i,j,visited):
        if i < 0 or i > rows - 1 or j <0 or j > cols - 1:
            return
        
        if grid[i][j] == '0' or visited[i][j] == True:
            return
        
        visited[i][j] = True
        
        dfsHelper(i+1, j, visited)
        dfsHelper(i-1, j, visited)
        dfsHelper(i, j+1, visited)
        dfsHelper(i, j-1, visited)
        
        
    connectedComponents = 0
    rows = len(grid)
    cols = len(grid[0])
    
    visited = []
    for row in range(rows):
        lst = []
        for col in range(cols):
            lst.append(False)
        visited.append(lst)
    
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] == False and grid[row][col] == '1':
                dfsHelper(row, col, visited)
                connectedComponents+=1
    
    return connectedComponents
```

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    indegrees = [0]*numCourses
    for prerequisite in prerequisites:
        graph[prerequisite[1]].append(prerequisite[0])
        indegrees[prerequisite[0]] += 1
    queue = []
    
    for i, x in enumerate(indegrees):
        if x == 0:
            queue.append(i)
    ans = []
    while len(queue) > 0:
        u = queue.pop(0)
        ans.append(u)
        for v in graph[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                queue.append(v)
    
    if len(ans) == numCourses:
        return ans
    else:
        return []
```