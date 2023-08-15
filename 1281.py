class Solution:
    def subtractProductAndSum(self, n):
        times=1
        sums=0
        for i in str(n):
            times=times*int(i)
            sums=sums+int(i)
        return times-sums
            