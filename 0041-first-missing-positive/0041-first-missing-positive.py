class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        digit = 1
        for i in nums:
            print(i,digit)
            if i>0:
                if digit<i:
                    return digit 
                digit+=1
        return digit
                
        
        
        
        