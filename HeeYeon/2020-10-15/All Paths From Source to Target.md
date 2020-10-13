### 797. All Paths From Source to Target
(주소)https://leetcode.com/problems/all-paths-from-source-to-target/

#### 풀이 해설:

dfs, backtraking

visited 필요 x


```c++
class Solution {
public:
    int n;
    vector<int> path[16];
    vector<vector<int>>answer;
    
    void dfs(int node, vector<int> v){
        if(node==n-1){
            answer.push_back(v);
            return;
        }
        
        for(int i=0;i<path[node].size();i++){
            v.push_back(path[node][i]);
            dfs(path[node][i], v);
            v.pop_back();
        }
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        n = graph.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<graph[i].size();j++){
                path[i].push_back(graph[i][j]);
            }
        }
        vector<int> v;
        v.push_back(0);
        
        dfs(0, v);
        
        return answer;
    }
};
```

---
