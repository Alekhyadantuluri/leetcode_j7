class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int c = -1;
        int v = 0;
        for(int i = 0; i < nums.size(); i++){
            if(v==0){
                c = nums[i];
                v+=1;
            }
            else{
                if(nums[i]==c){
                    v+=1;
                }
                else v-=1;
            }
            }
        return c;
        }
    
        
};