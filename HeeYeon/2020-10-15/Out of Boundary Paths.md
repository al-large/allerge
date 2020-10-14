### 576. Out of Boundary Paths
(주소)https://leetcode.com/problems/out-of-boundary-paths/

#### 풀이 해설:
 
dfs + DP


```c++
class Solution {
public:
    int row, col;
    int dir[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
    
    int dfs(int x, int y, int cnt, int N, vector<vector<vector<int>>>& dp){
        
        if(0>x || x>=row || 0>y || y>=col) {
            return 1;
        }
        
        if(cnt==N) return 0;
        
        if(dp[x][y][cnt]!=-1) return dp[x][y][cnt];
        
        dp[x][y][cnt]=0;
        for(int i=0;i<4;i++){
            int dx = x+dir[i][0];
            int dy = y+dir[i][1];
            
            dp[x][y][cnt] = (dp[x][y][cnt] + dfs(dx, dy, cnt+1, N, dp))%1000000007;
        }
        
        return dp[x][y][cnt];
    }
    
    int findPaths(int m, int n, int N, int i, int j) {
        row = m;
        col = n;
        
        vector<vector<vector<int>>> dp;
dp = vector<vector<vector<int>>>(m, vector<vector<int>>(n, vector<int>(N+1, -1)));
        
        return dfs(i,j,0,N,dp)%1000000007;
    }
};
```

---


