### 49. Group Anagrams
(주소)https://leetcode.com/problems/group-anagrams/

#### 풀이 해설:

해시맵을 이용


```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<pair<string,string>> s;
        map<string, vector<string>> mp;
        vector<vector<string>> answer;
        
        for(int i=0;i<strs.size();i++){
            string origin = strs[i];
            sort(strs[i].begin(), strs[i].end());
            string sorted = strs[i];
            s.push_back({origin, sorted});
        }
        for(int i=0;i<s.size();i++){
            mp[s[i].second].push_back(s[i].first);
        }
        map<string, vector<string>>::iterator it;
        
        for(it=mp.begin();it!=mp.end();it++){
            answer.push_back(it->second);
        }
        return answer;
    }
};
```

---
