class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        #if n is zero then it is empty graph empty graph is tree so we return True
        if not n:
            return True
        adj = {i: [] for i in range(n)} # we create map with node and their corresponding neighbors 
        #we traverse through every single pair of edges and add it to our adjency list with coresponding node
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set() #keep track of all node we visited

        def dfs(i, prev):
            #it means we detected loop we immediatly return False
            if i in visit:
                return False
            #if not then add it to visit set
            visit.add(i)
            #then traverse through every single neighbors of node i
            for j in adj[i]:
                #then we skip it
                if j == prev:
                    continue
                #if j doesn't equal to prev node then we call dfs on j and i is the prev value we are coming from
                #if it detect false we immediatly return False because that means we detected loop if it doesn't return False
                #then we go it it's other neighbors of node i
                if not dfs(j, i):
                    return False
            return True # if we go through every neighbors without detecting loop then we return True

        return dfs(0, -1) and n == len(visit) # we also check if graph is connected.

#Approch-> we will do standard dfs so for every single node we go on and visit it's neighbors recursively
#util we visited all neighbors that connected to 0 node at the end we check n== visited that means every node
#inside the graph is connected ,the other thing we check whether this graph doesn't contains cycle or loop
#if we encounter cycle then we return False immediatly we use visit set() and start from node 0 then add node 0 to set
#then we recursively go it's first neighbors 1 we then 1 to visit set now we notice 1 has 2 neighbors 2 and 4 node
#here we use prev value by setting prev=-1 as default at first for node 0, it keep track of it's previous visited node, so for node 1 prev node be 0 we can't go back to 0
#so from node 1 the only neighbors we visit is 4 and check it's already visited not then add it to visit set
#and 4 doesn't have neighbors so this will be base case for dfs and we return True because so far we didn't encounter a loop
#from 4 we go back to 1 and from 1 to node 0 since they have no more new neighbors then ,now from 0 we go to node 2
#and add node 2 in visit set and atlast we go from 0 to node 3 add 3 to visit set.after then we check if n== visited
#if it is false then we immediatly return False and also check whether it contains cycle by checking in visit setting
#if it contains cycle also then we immediatly return False.Time Complexity -> O(E+V)