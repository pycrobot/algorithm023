class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_1 in enumerate(nums):
            for j, num_2 in enumerate(nums):
                if i == j:
                    continue
                if num_2 + num_1 == target:
                    return [i, j]
