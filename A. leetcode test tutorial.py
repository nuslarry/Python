#leetcode 264. Ugly Number II
# test the program in local IDE eg: spyder
class Solution:

    def isUgly(self, n:int) -> int:
        while True:
            print("gg")
            if n%2==0:
                n/=2
                continue
            elif n%2==0:
                n/=3
                continue
            elif n%5==0:
                n/=5
                continue
        if n==1:
            return True
        else:
            return False
        
        
    def nthUglyNumber(self, n: int) -> int:
        ans=1
        cur=1
        testNum=2
        while cur<n:
            print(testNum)
            if self.isUgly(testNum):
                cur+=1
                ans=testNum
            testNum+=1
        return ans

s=Solution()
s.nthUglyNumber(10)
