from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in seen:
                return [seen[complemento], i]

            seen[num] = i