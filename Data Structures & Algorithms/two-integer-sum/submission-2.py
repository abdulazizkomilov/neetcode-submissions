class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in numDict:
                return [numDict[diff], idx]

            numDict[num] = idx
