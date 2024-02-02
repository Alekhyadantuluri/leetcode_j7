class Solution {
public:
    vector<int> sequentialDigits(int l, int h) {
        string s = "123456789";
        vector<int>ans;
        int low  = ((int)log10(l))+1;
        int high = ((int)log10(h))+1;
        for (int i = low ; i <= high ; i++){
            for(int j = 0 ; j < s.size()-(i-1) ; j++){
                int r = stoi(s.substr(j,i));
                if (r>=l and r<=h){
                ans.push_back(r);}
            }
        }
        return ans;
    }
};