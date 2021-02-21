class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        l = r = n

        def backtrack(l, r, tmp):
            if l == r == 0:
                res.append(tmp)
                return
            if l > r:
                return
            if l > 0:
                backtrack(l-1, r, tmp + "(")
            if r > 0:
                backtrack(l, r-1, tmp + ")")
        backtrack(l, r, "")
        return res