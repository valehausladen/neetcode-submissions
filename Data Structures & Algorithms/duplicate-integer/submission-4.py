class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        if len(sorted_nums) == 1:
            return False
        for index, num in enumerate(sorted_nums):
            if sorted_nums[index-1] == num:
                return True
        return False