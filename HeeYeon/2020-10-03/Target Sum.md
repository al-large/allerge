### 494. Target Sum

(주소)https://leetcode.com/problems/target-sum/



#### 문제 요약:

각 숫자들에 + 나 - 부호를 붙여서 합이 target이 되는 조합 개수 구하는 문제.


#### 풀이 해설:

숫자들 위치는 고정된 상태에서 +와 -의 순서 및 조합만 모든 경우의 수에 따라 검사해봄. -> dfs로 완전탐색.

```c++
class Solution {
public:
    int answer = 0;
    
    void dfs(int sum, int idx, vector<int>& nums, int S) {
        if(idx == nums.size()){
            if(sum==S) answer++;
            return;
        }
        dfs(sum + nums[idx], idx+1, nums, S);
        dfs(sum - nums[idx], idx+1, nums, S);
    }
    
    int findTargetSumWays(vector<int>& nums, int S) {
        int tol=accumulate(nums.begin(),nums.end(),0);
        if(tol<S) return 0;

        dfs(0,0,nums,S);
        return answer;
    }
};
```
---
