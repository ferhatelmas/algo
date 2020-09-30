from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    cnt += 1
                if j == 0 or row[j - 1] == 0:
                    cnt += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    cnt += 1
                if j == len(row) - 1 or row[j + 1] == 0:
                    cnt += 1
        return cnt
    /*class Solution {
public:
    int cnt=0;
    void dfs(vector<vector<int>>& grid,int i,int j)
    {
        if(i<0||i>=grid.size()||j<0||j>=grid[i].size()||grid[i][j]==0)
        {
            cnt++;
            return;
        }
        if(grid[i][j]==-1) return;
        grid[i][j]=-1;
        dfs(grid,i-1,j);
        dfs(grid,i+1,j);
        dfs(grid,i,j-1);
        dfs(grid,i,j+1);
    }
    int islandPerimeter(vector<vector<int>>& grid) {
        cnt=0;
        //int n=grid.size(),m=grid[0].size();
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[i].size();j++)
            {
                if(grid[i][j]==1)
                {
                    dfs(grid,i,j);
                   break;
                }
            }
        }
        return cnt;
    }
};*/
