class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS,COLS = len(grid1),len(grid1[0])
        visit = set() #keep track of visited cells
        def dfs(r,c):
            if (r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or (r,c) in visit):  #if we are reached outofbound or we reach the water or we already visited the cells we return true becuase we return false only when grid1 has water not grid2 
                return True
            visit.add((r,c))
            res = True
            if grid1[r][c] ==0: #if grid1 is water then return false if any single1 island is missing in grid1 then we return False immediatly.
                res = False
            #Run dfs in all 4 directions if any of these 4 dfs function recursively return false then we return False.
            res = dfs(r-1,c) and res 
            res = dfs(r+1,c) and res
            res = dfs(r,c-1) and res
            res = dfs(r,c+1) and res
            return res
            
            
            
        count=0   
        for r in range(ROWS):
            for c in range(COLS): #go to every row and cols in the grid
                if grid2[r][c] and (r,c) not in visit and dfs(r,c): #if it is land in grid2 and it is not visited yet then we call dfs in this cordinates means we just found an unvisited island we just ran dfs on if it have to be any corresponding island in grid1 then we increment the count by +1
                    count+=1 #increase count by 1
        return count