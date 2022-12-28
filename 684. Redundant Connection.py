class Solution:        
    def bfs(self,node,parent,graph,visited):
        q = deque()
        q.append(node)
        visited.add(node)
        while q:
            node = q.popleft()
            if node == parent:
                return True
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append(child)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n= len(edges)
        graph = defaultdict(list)
        for i ,j in edges:
            if self.bfs(i,j,graph,set()):
                return [i,j]
            graph[i].append(j)
            graph[j].append(i)