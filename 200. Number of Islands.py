class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: # if it is empty grid we don't need to run our algorithm
            return 0
        rows =len(grid)
        cols = len(grid[0])
        visit = set() #to keep track f visisted cells
        Isisland=0
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q: # while q is not empty
                row,col = q.popleft() # we pop from queue
                #check the adjecent position of the position we just pop we use loop to check it's adjecent in all 4 direction
                direction = [[1,0],[-1,0],[0,1],[0,-1]]

                #now for each of these directions
                for dr,dc in direction:
                    r,c = row+dr , col+dc
                    #we check whether they are inbound
                    if((r) in range(rows) and (c) in range(cols) and grid[r][c]=="1" and (r,c)
                    not in visit):
                        #if it is true then we need to add it to q to run bfs on this cell as well
                        q.append((r,c))
                        visit.add((r,c))



        #itetrate every single row and col of grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and (r,c) not in visit: 
                    bfs(r,c) # call bfs
                    Isisland+=1
        return Isisland



