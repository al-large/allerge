### 518. Coin Change 2
(주소)https://leetcode.com/problems/coin-change-2/

#### 풀이 해설:



```c++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int dp[amount+1];
        for(int i=0;i<amount+1;i++){
            dp[i]=0;
        }
        
        dp[0]=1;
        for(int i=0;i<coins.size();i++){
            for(int j=coins[i];j<=amount;j++){
                dp[j]+=dp[j-coins[i]];
            }
        }
        return dp[amount];
    }
};
```
