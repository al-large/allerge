### 648. Replace Words
(주소)https://leetcode.com/problems/replace-words/

#### 풀이 해설:

trie를 이용하여 문자열을 탐색한다.  일치하는 접두어를 만나면 문자열을 그 접두어로 대체한다. 


```c++
const int ALPABATS = 26;
 
class Tri_Node {
public:
    Tri_Node * child[ALPABATS];
    bool finish = false;
 
 
    Tri_Node() {
        for (int i = 0; i < ALPABATS; i++)
            child[i] = NULL;
    }
 
    ~Tri_Node() {
        for (int i = 0; i < ALPABATS; i++)
            delete child[i];
    }
    
    void insert(string s, int idx = 0) {
        if (s[idx] == '\0')  //입력받은 words가 '\0'일 경우, 즉 문자열 끝인 경우.
            finish = true;
 
        else {
            if (child[s[idx]-'a'] == NULL) {
            child[s[idx]-'a'] = new Tri_Node();
            }
            child[s[idx]-'a']->insert(s,idx+1);
        }
    }
    
    bool find(string s, int idx = 0) {
        if (s[idx] == '\0' && finish)
            return true;
 
        if (child[s[idx]-'a'] == NULL)
            return false;
 
        return child[s[idx]-'a']->find(s,idx+1);
    }
    
    void replace(string &s, int idx = 0) {
        if (s[idx] == '\0')
            return;
        else if(finish){
            s = s.substr(0,idx);
        }
        else if(child[s[idx]-'a']!=NULL){
            child[s[idx]-'a']->replace(s,idx+1);
        }
        
    }
    
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        string answer = "";
        Tri_Node* root = new Tri_Node();
		for (int i=0;i<dictionary.size();i++){
            root->insert(dictionary[i]);
        }
        
        string s = "";
        for(int i=0;i<sentence.size();i++){
            if(sentence[i]==' '){
                root->replace(s);
                answer += s + " ";
                s = "";
            }
            else s+=sentence[i];
        };
        
        if(s != "") {
            root->replace(s);
            answer+=s;
        }
        
        return answer;
    }
};
```

---
