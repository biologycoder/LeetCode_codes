class Solution:
    def addDigits(self, num):
        while len(str(num))>1:
            num=self.plus(num)
        return num
    def plus(self,digit):
        result=0
        for i in str(digit):
            result+=int(i)
        return result