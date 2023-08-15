class Solution:
    def vowelStrings(self,words,left,right):
        cnt=0
        for i in range(left,right+1):
            if self.isyuan(words[i]):
                cnt+=1
        return cnt
    def isyuan(self,word):
        yuanli = ['a','e','i','o','u']
        if word[0] in yuanli and word[-1] in yuanli:
            return True
        else:
            return False