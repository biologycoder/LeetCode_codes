class Solution:
    def shuffle(self, nums, n):
        ans=[]
        x=nums[0:n]
        y=nums[n:2*n]
        for i in range(n):
            ans.append(x[i])
            ans.append(y[i])
        return ans