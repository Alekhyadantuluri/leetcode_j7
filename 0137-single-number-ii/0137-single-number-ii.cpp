class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int>a(32,0);
        int c  = 0;
        for(int i = 0 ; i < nums.size() ;i++){
            if (nums[i]<0){
                c+=1;
                nums[i]=abs(nums[i]);
            }
            for(int j = 0 ; j < 32 ; j++){
                if((1<<j) & nums[i]){
                    a[j]+=1;
                }
            }   
        }
        int b  = 0;
        for(int i = 0 ; i < 32 ;i++){
         b+=(a[i]%3)*(1<<i)   ;
        }
        long long w = -1;
        if (c%3!=0) return w*b;
        else return b;
    }
};