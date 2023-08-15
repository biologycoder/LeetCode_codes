class Solution:
    def isPowerOfThree(self, n):
        if n==1:
            return True
        while n>1 and n%3==0:
            n//=3
            if n==1:
                return True
        return False