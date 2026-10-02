class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        while j <= len(nums) - 1:
            for num in range(j, len(nums)):
                if nums[i] + nums[num] == target:
                    return [i, num]

            i += 1
            j += 1

        return [i, j]
