from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}  # Initialize an empty dictionary to store numbers and their indices.
        n = len(nums)  # Get the length of the input list nums.

        for i in range(n):
            complement = target - nums[i]
            # Check if the complement exists in numMap. If it does, it means we have found a pair of numbers whose sum equals the target.
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
