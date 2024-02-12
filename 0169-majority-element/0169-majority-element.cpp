class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int>d;
        int a = 0;
        for(int i = 0; i < nums.size(); i++){
            d[nums[i]]+=1;
            if (d[nums[i]] > nums.size()/2) {
                a = nums[i];
                break;
            }
        }
        return a;
    }
};