class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        cnt=0
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i>=j:
                    continue
                else:
                    for k in range(0,len(arr)):
                        if j>=k:
                            continue
                        else:
                            if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                                cnt+=1
        return cnt