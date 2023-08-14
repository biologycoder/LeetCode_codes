class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = int(a,2),int(b,2)
        result = bin(a+b)
        ans = ''
        for i in range(len(result)):
            if i == 0 or i == 1:
                continue
            ans = ans+result[i]
        return ans