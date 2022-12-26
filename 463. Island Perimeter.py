class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set() #keep track of visited cell
        def dfs(i,j): #cordinates of cell we visiting
            if i>= len(grid) or j>= len(grid[0]) or i<0 or j<0 or grid[i][j]==0:
                #condition for outof bound
                return 1
            if (i,j) in visit: # check if it already visited
                return 0
            visit.add((i,j)) # we don't have to visit i and j multiple time while makin recursive call
            #making dfs recursive call in all 4 direction
            perim = dfs(i,j+1)
            perim+= dfs(i+1,j)
            perim+= dfs(i,j-1)
            perim+= dfs(i-1,j)
            return perim
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j) #then we return the result of dfs