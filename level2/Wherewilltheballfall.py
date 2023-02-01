class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):
            if i == rows:return j #if you reach the last row, return column
            if j == cols -1 and grid[i][j] == 1: return -1
            if j == 0 and grid[i][j] ==-1:return -1
            if grid[i][j] ==1 and grid[i][j+1] == -1 :return -1
            if grid[i][j] ==-1 and grid[i][j-1]==1:return -1
            return dfs(i+1, j+grid[i][j])
        return [dfs(0,j) for j in range(cols)]

