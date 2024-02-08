class Solution {
public:
    int dp[10001];
    int ways(int n,int mini){
        if (n==0) return 0;
        if (dp[n]!=-1) return dp[n];
        for(int i = 1 ; i <= (int)sqrt(n) ;i++){
            int a = i*i;
            if (n>=a){ 
                // cout << c << " ";
                int c=1+ways(n-a,mini);
                mini = min(mini,c);
            }
        }
        return dp[n]=mini;
    }
    int numSquares(int n) {
        vector<int>nums;
        memset(dp,-1,sizeof(dp));
        int c = 0;
        int mini = INT_MAX;
        return ways(n,mini);
        
    }
};