class Solution:
    def intersection(self, nums1, nums2):
        s1,s2=set(nums1),set(nums2)
        return list(s1 & s2)
