class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            ans = [1 for _ in range(i+1)]
            for j in range(1,(i//2)+1):
                ans[j] = res[-1][j-1]+res[-1][j]
                ans[i-j] = ans[j]
            res.append(ans)
        return res