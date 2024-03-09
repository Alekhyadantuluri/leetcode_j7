class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l= sorted(list(set(nums1).intersection(set(nums2))))
        if l==[]:
            return -1
        return l[0]