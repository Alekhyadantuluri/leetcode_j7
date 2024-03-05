class Solution {
public:
    int minimumLength(string s) {
        int i=0;
        int j=s.size()-1;
        while(i<j and s[i]==s[j]){
                while(i+1<j and s[i]==s[i+1]) i++;
                while(i<j-1 and s[j]==s[j-1]) j--;
            i+=1;
            j-=1;
        }
        return j-i+1;
    }
};