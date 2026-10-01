"""
0, 1.   1, 2.   2, 3.  3, 4
0, 2.   1, 3.   2, 4
0, 3.   1, 4
0, 4
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicateNums = set()
        for num in nums:
            if num in noDuplicateNums:
                return True
            else:
                noDuplicateNums.add(num)
        return False
