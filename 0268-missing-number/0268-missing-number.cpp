class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int a=0;
        for(int i = 0; i < nums.size() ;i++){
            a = a ^ nums[i];
            a= a ^ (i+1);
        }
        cout << a;
        return a;
    }
};