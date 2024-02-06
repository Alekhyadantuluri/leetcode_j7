class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>>ans;
        vector<vector<string>>g;
        for(int i =  0 ; i < strs.size() ; i++){
            string word = strs[i];
            sort(word.begin(),word.end());
            ans[word].push_back(strs[i]);
        }
        for(auto it:ans){
            g.push_back(it.second);        }
        return g;
    }
};