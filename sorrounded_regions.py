class Solution:
    def dfs(self , r , c , visited , rows , cols , barrier):
        visited[r][c] = 1
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if barrier[r][c] == "x":
            return
        if visited[r][c] == 1:
            return
        self.dfs(r-1 ,c , visited , rows , cols , barrier)
        self.dfs(r , c-1 , visited , rows , cols , barrier)
        self.dfs(r , c+1 , visited , rows , cols , barrier)
        self.dfs(r+1 ,c , visited , rows , cols , barrier)        

    def sorround_region(self , barrier , visited , rows , cols):
        # Upper row :
        r , c = 0 , 0 
        for c in range(cols):
            if barrier[r][c] == "O" :
                if visited[r][c] == 0:
                    self.dfs(r , c , visited , rows , cols , barrier)
        # Last row :
        r , c = rows -1 , 0
        for c in range(cols):
            if barrier[r][c] == "O" :
                if visited[r][c] == 0:
                    self.dfs(r , c , visited , rows , cols , barrier)
        # First column :
        r , c = 0 , 0
        for r in range(rows):
            if barrier[r][c] == "O" :
                if visited[r][c] == 0:
                    self.dfs(r , c , visited , rows , cols , barrier)
        # Last column :
        r , c = cols -1 , 0
        for c in range(cols):
            if barrier[r][c] == "O" :
                if visited[r][c] == 0:
                    self.dfs(r , c , visited , rows , cols , barrier)
       # Updating unmarked Os to x                   
        for r in range(rows):
                for c in range(cols):
                    if barrier[r][c] == "O" and visited[r][c] == 0:
                        barrier[r][c] = "x"

barrier = [ 
    [ "x" , "x" , "x" , "x" , "x"] ,
    [ "x" , "O" , "O" , "x" , "x"] ,
    [ "x" , "O" , "O" , "x" , "x"] ,
    [ "x" , "O" , "O" , "x" , "x"] ,
    [ "x" , "x" , "x" , "x" , "x"]
]
rows = len(barrier)
cols = len(barrier[0])
visited = [[0 for _ in range(rows)] for _ in range(cols)]
sol = Solution()
res = sol.sorround_region(barrier , visited,  rows , cols)
print(barrier)
