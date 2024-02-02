class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        stack<pair<int,int>>st;
        int n = t.size();
        vector<int>in(n,0);
        st.push({t[n-1],n-1});
        for(int i = n-2 ; i > -1 ; i--){
            while (!st.empty() && t[i]>=st.top().first){
                st.pop();
            }
            if (!st.empty()){
            in[i]=abs(st.top().second-i);}
            st.push({t[i],i});
    }
        return in;
    }
};