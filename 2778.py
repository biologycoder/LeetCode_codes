class Solution:
    def sumOfSquares(self, nums):
        ans=0
        for i in range(1,len(nums)+1):
            if len(nums)%i==0:
                ans+=nums[i-1]**2
        return ans