class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights),len(heights[0])
        pac,atl = set(),set() # 2 hashset for pacific and atlantic respectively
        
        def dfs(r,c,visit,preHeight):
            #already visited or outofbounds and height is less then prev height 
            if ((r,c) in visit or r<0 or c<0 or r==ROWS or c==COLS or heights[r][c]<preHeight):
                return
            #if above conditions are false we are finging new cells add to visit set
            visit.add((r,c))
            #run dfs on it's all 4 neighbors
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c]) #first row
            dfs(ROWS-1,c,atl,heights[ROWS-1][c]) #last row
            
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0]) #1st column
            dfs(r,COLS-1,atl,heights[r][COLS-1]) # last column
        
        res =[]
        # itetrate the grid
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res