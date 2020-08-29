### Number of Steps to Reduce a Number in Binary Representation to One
(주소)https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

#### 풀이 해설:

1101. (13)

1110. (14)+1.  111 , 1000(없앤 1 개수만큼 0을 더함), 100, 10, 1

111  (7) +1

1000. (8) +1

100. (4). +1

10. (2). +1

1. (1). +1

= +6


```c++
class Solution {
public:
    int numSteps(string s) {
        stack<char>st;
        int answer = 0;
        
        for(int i=0;i<s.size();i++){
            st.push(s[i]);
        }
        
        
        if(st.size()<=1) return 0;
        
        while(1){
            if(st.size()==1) break;
            if(st.top()=='0'){
                answer++;
                st.pop();
            }
            else if(st.top()=='1'){
                int n =0;
                while(st.size()>0 && st.top()!='0'){  // 느낀점: stack 비었을때 top 접근안하도록 주의하자.
                    st.pop();
                    n++;
                }
                if(st.size()>0) st.pop();
                st.push('1');
                for(int i=0;i<n;i++){
                    st.push('0');
                }
                answer++;
            }
        }
        
        return answer;
    }
};
```

---
