### 79. Word Search
(주소)https://leetcode.com/problems/word-search/

#### 풀이 해설:

dfs로 문자열 원소를 하나씩 찾아나감. 그치만 마지막 테케에서 시간초과 발생…

```c++
class Solution {
public:
    int n, m;
    bool answer = false;
    bool visited[201][201];
    int dir[4][2] = {{1,0},{0,-1},{-1,0},{0,1}};
    
    void dfs(int x, int y, int idx, string word, vector<vector<char>>& board){
        if(idx == word.size()){
            answer = true;
            return;
        }
        for(int i=0;i<4;i++){
            int dx = x + dir[i][0];
            int dy = y + dir[i][1];
            if(0<=dx && dx<n && 0<=dy && dy<m){
                if(visited[dx][dy]==false && board[dx][dy]==word[idx]){
                    visited[dx][dy]=true;
                    dfs(dx,dy,idx+1,word,board);
                    visited[dx][dy]=false;
                }
            }
        }
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        n = board.size();
        m = board[0].size();
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(board[i][j] == word[0]){
                    visited[i][j]=true;
                    dfs(i,j,1,word, board);
                    visited[i][j]=false;
                }
            }
        }
        return answer;
    }
};
```

---
