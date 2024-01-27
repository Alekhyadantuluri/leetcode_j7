class Solution {
public:
    void comb(int i,int n,int k,vector<int>&arr,vector<vector<int>>&main,vector<int>&ds ){
        if (i==n){
            if (k==0){
                main.push_back(ds);
            }
            return;
        }
        if(arr[i]<=k){
            ds.push_back(arr[i]);
            k=k-arr[i];
            comb(i,n,k,arr,main,ds);
            k=k+arr[i];
            ds.pop_back();
        }
        comb(i+1,n,k,arr,main,ds);
        return;
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>main;
        vector<int>ds;
        comb(0,candidates.size(),target,candidates,main,ds);
        return main;
    }
};