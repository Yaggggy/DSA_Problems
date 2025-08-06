class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        seta = set(nums1)
        setb = set(nums2)
        minn = seta.intersection(setb)
        if len(minn) > 0 :
            return int(min(minn))
        
        min_a = min(seta)
        min_b = min(setb)

        if min_a < min_b :
            return int(str(min_a)+ str(min_b))
        else:
            return  int(str(min_b)+ str(min_a))
