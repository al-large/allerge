### 377. Combination Sum IV
(주소)https://leetcode.com/problems/combination-sum-iv/

#### 풀이 해설:


```c++
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int n = nums.size();
        
        unsigned int dp[target+1];
        for(int i=0;i<=target;i++){
            dp[i]=0;
        }
        dp[0]=1;
        
        for(int i=1;i<=target;i++){
            for(int j=0;j<n;j++){
                if(i>=nums[j]) dp[i]+=dp[i-nums[j]];
            }
        }
        
        return dp[target];
    }
};
```

---

