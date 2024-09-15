from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self._sum = 0
        self.prefix_sum = {i: 0 for i in range(len(nums))}
        total_sum = 0
        for index, nums in enumerate(nums):
            total_sum += nums
            self.prefix_sum[index] = total_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - (self.prefix_sum[left-1] if left-1 >=0 else 0)