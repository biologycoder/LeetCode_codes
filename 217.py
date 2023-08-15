class Solution:
    def containsDuplicate(self, nums):
        copy = set(nums)
        if len(list(copy)) == len(nums):
            return False
        else:
            return True
