class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit =set() #keep track of visited cells
        direction =[[0,1],[0,-1],[1,0],[-1,0]] #to get 4 directions
        def invalid(r,c): #to check if cordinates gone out of bounds it returns outof bounds
            return  r<0 or c< 0 or r == N or c==N 
        
        def dfs(r,c):
            #check if row and cols are outof bounds or if it is water or r,c already in visit set
            if(invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return
            #if it is not outof bounds or water or not added to visit set then we add it to set
            visit.add((r,c))
            #run dfs in all 4 directions
            for dr,dc in direction:
                dfs(r+dr,c+dc)
            
        def bfs():
            res=0 # determine lenght of the bridges
            q = deque(visit) # initilize with visit hashset values
            #implement standard bfs algorithms
            while q:
                #we go to each layer one ny one and increment res while traversing each layer
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in direction:
                        curR,curC = r+dr,c+dc
                        #check if we are out of bounds or curR,curC already been visited before
                        if invalid(curR,curC) or (curR,curC) in visit:
                            continue # then we gonna to continue next itetration of loop just skip it
                        #if we reach to other island and it is inbound then we return result 
                        if grid[curR][curC]:
                            return res

                        #if it is water
                        q.append([curR,curC])
                        visit.add((curR,curC))
                res+=1 # every for loop itertate over the layer of water



        #itetrate over entire input grid
        for r in range(N):
            for c in range(N):
                #if we get to island first time then run dfs on it because it gonna fill hashset with one of the island
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()