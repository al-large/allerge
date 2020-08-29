### Perfect squares

(주소)https://leetcode.com/problems/perfect-squares/



#### 풀이:

```c++
class Solution {
public:
    int numSquares(int n) {
        int dp[n+1];
        dp[0]=0;
        for(int i=0;i<=n;i++){  // 초기화
            dp[i]=0;
        }
        
        int num = 1;
        while(num*num<=n){
            dp[num*num]=1;  // 제곱수의 dp값은 1
            num++;
        }
        
        for(int i=2;i<=n;i++){
            if(dp[i]!=1) {  // 제곱수는 제외
                int newVal = dp[1] + dp[i-1];
                for(int j=2;j*j<i;j++){
                    newVal = min(newVal, dp[j*j]+dp[i-j*j]);
                }
                dp[i]=newVal;
            }
        }
        return dp[n];
    }
};

//dp[1]=1, dp[4]=1, dp[9]=1,,,,, dp[13]=dp[4]+dp[9] minimun
// dp[8]=dp[4]+dp[4]=2
//dp[12]=dp[4]+dp[8]=3


// 5 : 1,4/2,3/3,2/4,1,,,,,5/2=2
//6: 1,5/2,4/3,3/4,2/5,1,,,,,,6/2=3

```
---
