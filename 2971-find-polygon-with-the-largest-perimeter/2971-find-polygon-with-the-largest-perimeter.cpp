class Solution {
public:
    int mod = 1e9+7;
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        long long sum = 0;
        for(int i = 0 ; i < nums.size() ; i++){
            sum += nums[i];
        }
        int i = nums.size()-1;
        while(i>1){
            if (sum-nums[i]<=nums[i]){
                sum-=nums[i];
            }
            else{
                return sum;
            }
            i-=1;
        }
        return -1;
        }
};