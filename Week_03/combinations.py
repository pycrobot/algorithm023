class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """回溯法"""
        nums = [i for i in range(1, n+1)]
        res = []
        if n==0 or k==0:
            return res
        def backtrace(nums_b,curr_res,index):
            if len(curr_res)==k:
                res.append(curr_res[:])
                return
            for i in range(index,n):
                curr_res.append(nums[i])
                backtrace(nums_b[index:],curr_res,i+1)
                curr_res.pop()
        backtrace(nums,[],0)
        return res