class Solution:
    def separateDigits(self, nums):
        ans = []
        for i in nums:
            for j in str(i):
                ans.append(int(j))
        return ans
