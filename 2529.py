class Solution:
    def maximumCount(self, nums):
        over0=0
        below0=0
        for n in nums:
            if n > 0:
                over0 += 1
            elif n < 0:
                below0 += 1
        if over0 >= below0:
            return over0
        else:
            return below0