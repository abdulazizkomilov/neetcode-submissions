"""
O(n²)
0, 1.   1, 2.   2, 3.  3, 4
0, 2.   1, 3.   2, 4
0, 3.   1, 4
0, 4

O(1)
[1, 2, 3, 4]
[1, 2, 2, 3]

{1, 2, 3, 4} -> false

{1, 2} -> true
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonDuplicate = set()
        for num in nums:
            if num in nonDuplicate:
                return True
            nonDuplicate.add(num)
        return False
